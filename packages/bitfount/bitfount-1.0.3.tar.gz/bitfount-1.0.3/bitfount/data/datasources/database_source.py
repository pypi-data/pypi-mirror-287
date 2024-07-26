"""Module containing DatabaseSource class.

DatabaseSource class handles loading data stored in a SQL database.
"""

from __future__ import annotations

from functools import wraps
import logging
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Union, cast

import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import MetaData, Table, text
from sqlalchemy.engine import Row
from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import Session

from bitfount.config import BITFOUNT_TASK_BATCH_SIZE
from bitfount.data.datasources.base_source import IterableSource, MultiTableSource
from bitfount.data.exceptions import DatabaseInvalidUrlError
from bitfount.data.utils import (
    DatabaseConnection,
    _convert_python_dtypes_to_pandas_dtypes,
)
from bitfount.types import _Dtypes
from bitfount.utils import delegates

logger = logging.getLogger(__name__)


# The default buffer size on the client side. This is significantly larger than the
# partition size to ensure there is no data transfer bottleneck during iteration.
_DATABASE_MAX_ROW_BUFFER: int = 500


def auto_validate(f: Callable) -> Callable:
    """Decorator which validates the database connection."""

    @wraps(f)
    def wrapper(self: DatabaseSource, *args: Any, **kwargs: Any) -> Any:
        if not self._con:
            self.validate()
        return f(self, *args, **kwargs)

    return wrapper


@delegates()
class DatabaseSource(MultiTableSource, IterableSource):
    """Data source for loading data from databases.

    This datasource subclasses both MultiTableSource and IterableSource. This means
    that it can be used to load data from a single table or multiple tables. It also
    means that it can be used to load data all at once or iteratively. However, these
    two functionalities are mutually inclusive. If you want to load data from multiple
    tables, you must use the iterable functionality. If you want to load data from a
    single table, you must use the non-iterable functionality.
    """

    def __init__(
        self,
        db_conn: Union[DatabaseConnection, str],
        partition_size: int = BITFOUNT_TASK_BATCH_SIZE,
        max_row_buffer: int = _DATABASE_MAX_ROW_BUFFER,
        db_conn_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ):
        super().__init__(partition_size=partition_size, **kwargs)

        if isinstance(db_conn, DatabaseConnection):
            self.db_conn: DatabaseConnection = db_conn
        else:
            if not db_conn_kwargs:
                db_conn_kwargs = {}
            self.db_conn = DatabaseConnection(db_conn, **db_conn_kwargs)

        self.max_row_buffer = max_row_buffer
        self._con: Optional[sqlalchemy.engine.Engine] = None
        self.datastructure_query: Optional[str] = None
        self.datastructure_table_name: Optional[str] = None

    def validate(self) -> None:
        """Validate the database connection.

        This method does not revalidate the connection if it has already
        been validated.

        Raises:
            ArgumentError: If the database connection is not a valid sqlalchemy
                database url.
        """
        try:
            self.db_conn.validate()
        except ArgumentError as ex:
            url = "https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls"
            if isinstance(self.db_conn.con, str):
                raise DatabaseInvalidUrlError(
                    f"Invalid db_conn. db_conn: {self.db_conn.con} must be sqlalchemy "
                    f"compatible database url, see: {url}. "
                ) from ex
            raise

    @property
    def iterable(self) -> bool:
        """Defines whether the data source is iterable.

        For the database source, it can only be iterable if `multi_table` is True.
        """
        return self.multi_table

    @property
    @auto_validate
    def multi_table(self) -> bool:
        """Attribute to specify whether the datasource is multi table.

        This returns True if the database connection has multiple tables and no query
        is provided when creating the datasource.
        """
        return self.db_conn.multi_table

    @property
    @auto_validate
    def table_names(self) -> List[str]:
        """Database table names."""
        return cast(List[str], self.db_conn.table_names)

    @property
    @auto_validate
    def query(self) -> Optional[str]:
        """A Database query as a string.

        The query is resolved in the following order:
            1. The query specified in the database connection.
            2. The table name specified in the database connection if just 1 table.
            3. The query specified by the datastructure (if multi-table).
            4. The table name specified by the datastructure (if multi-table).
            5. None.
        """
        if self.db_conn.query:
            return self.db_conn.query
        elif self.db_conn.table_names and len(self.db_conn.table_names) == 1:
            # Table name has been validated
            return f"SELECT * FROM {self.db_conn.table_names[0]}"  # nosec hardcoded_sql_expressions # noqa: B950
        elif self.datastructure_query:
            return self.datastructure_query
        elif self.datastructure_table_name:
            # Table name has been validated
            return f"SELECT * FROM {self.datastructure_table_name}"  # nosec hardcoded_sql_expressions # noqa: B950

        return None

    @property
    @auto_validate
    def con(self) -> sqlalchemy.engine.Engine:
        """Sqlalchemy engine.

        Connection options are set to stream results using a server side cursor where
        possible (depends on the database backend's support for this feature) with a
        maximum client side row buffer of `self.max_row_buffer` rows.
        """
        if not self._con:
            assert not isinstance(self.db_conn.con, str)  # nosec assert_used
            self._con = self.db_conn.con.execution_options(
                stream_results=True, max_row_buffer=self.max_row_buffer
            )
        return self._con

    def __len__(self) -> int:
        if self._data_is_loaded:
            return len(self.data)
        elif not self.multi_table:
            data = self.get_data()
            assert data is not None  # nosec assert_used
            return len(data)

        with self.con.connect() as con:
            # Ignoring the security warning because the sql query is trusted and
            # will be executed regardless.
            result = con.execute(
                text(
                    f"SELECT COUNT(*) FROM ({self.query}) q"  # nosec hardcoded_sql_expressions # noqa: B950
                )
            )
            return cast(int, result.scalar_one())

    def _validate_table_name(self, table_name: str) -> None:
        """Validate the table name exists in the database.

        Args:
            table_name: The name of the table.

        Raises:
            ValueError: If the table name is not found in the data.
            ValueError: If the database connection does not have any table names.
        """
        if not self.table_names:
            raise ValueError("Database Connection is not aware of any tables.")
        elif table_name not in self.table_names:
            raise ValueError(
                f"Table name {table_name} not found in the data. "
                f"Available tables: {self.table_names}"
            )

    @auto_validate
    def get_values(
        self, col_names: List[str], table_name: Optional[str] = None, **kwargs: Any
    ) -> Dict[str, Iterable[Any]]:
        """Get distinct values from columns in Database dataset.

        Args:
            col_names: The list of the columns whose distinct values should be
                returned.
            table_name: The name of the table to which the column exists. Required
                for multi-table databases.

        Returns:
            The distinct values of the requested column as a mapping from col name to
            a series of distinct values.
        """
        metadata = MetaData(self.con)
        output: Dict[str, Iterable[Any]] = {}
        if self.query is not None:
            # TODO: [BIT-1595] change to load memory using sqlalchemy FrozenResult
            data = pd.read_sql(self.query, con=self.con)
            for col_name in col_names:
                output[col_name] = data[col_name].unique()
        elif table_name is not None:
            self._validate_table_name(table_name)

            table = Table(
                table_name,
                metadata,
                schema=self.db_conn.db_schema,
                autoload=True,
                autoload_with=self.con,
            )
            with Session(self.con) as session:
                for col_name in col_names:
                    values = np.array(
                        [v for v, in session.query(table.columns[col_name]).distinct()]
                    )
                    output[col_name] = values
        else:
            raise ValueError("No table name provided for multi-table datasource.")
        return output

    def get_column_names(
        self, table_name: Optional[str] = None, **kwargs: Any
    ) -> Iterable[str]:
        """Get the column names as an iterable.

        Args:
            table_name: The name of the table_name which should be loaded. Only
                required for multitable database.

        Returns:
            A list of the column names for the target table.

        Raises:
            ValueError: If the data is multi-table but no table name provided.
        """
        metadata = MetaData(self.con)

        if self.query is not None:
            with Session(self.con) as session:
                result: Row = cast(Row, session.execute(text(self.query)).first())
            return result.keys()
        elif table_name is not None:
            self._validate_table_name(table_name)

            table = Table(
                table_name,
                metadata,
                schema=self.db_conn.db_schema,
                autoload=True,
                autoload_with=self.con,
            )
            return list(table.columns.keys())
        else:
            raise ValueError("No table name provided for multi-table datasource.")

    @auto_validate
    def get_column(
        self, col_name: str, table_name: Optional[str] = None, **kwargs: Any
    ) -> pd.Series:
        """Loads and returns single column from Database dataset.

        Args:
            col_name: The name of the column which should be loaded.
            table_name: The name of the table to which the column exists. Required
                for multi-table databases.

        Returns:
            The column requested as a series.

        Raises:
            ValueError: If the data is multi-table but no table name provided.
            ValueError: If the table name is not found in the data.
        """
        results: Iterable[Any]
        metadata = MetaData(self.con)
        if self.query is not None:
            with Session(self.con) as session:
                results = session.execute(text(self.query)).columns(col_name)
        elif table_name is not None:
            self._validate_table_name(table_name)

            table = Table(
                table_name,
                metadata,
                schema=self.db_conn.db_schema,
                autoload=True,
                autoload_with=self.con,
            )
            with Session(self.con) as session:
                results = session.query(table.columns[col_name])
        else:
            raise ValueError("No table name provided for multi-table datasource.")
        series: pd.Series = pd.Series([v for v, in results])
        return series

    @auto_validate
    def get_data(
        self,
        table_name: Optional[str] = None,
        sql_query: Optional[str] = None,
        **kwargs: Any,
    ) -> Optional[pd.DataFrame]:
        """Loads and returns data from Database dataset.

        Args:
            sql_query: A SQL query string required for multi table data sources. This
                comes from the DataStructure and takes precedence over the table_name.
            table_name: Table name for multi table data sources. This
                comes from the DataStructure and is ignored if sql_query has been
                provided.

        Returns:
            A DataFrame-type object which contains the data or None if the data is
            multi-table.
        """
        data: Optional[pd.DataFrame] = None
        if self.iterable:
            # If multi-table, we don't actually load the data, we just set the query and
            # table name for the iterator. We then intentionally return None.
            if sql_query is not None:
                self.datastructure_query = sql_query
            if table_name is not None:
                self.datastructure_table_name = table_name
            return None

        elif self.db_conn.query:
            data = pd.read_sql_query(sql=self.db_conn.query, con=self.con)
        else:
            # If the data is not multi-table and there is no query, there must
            # necessarily be one table name. Reassuring mypy of this.
            assert (
                self.table_names is not None and len(self.table_names) == 1
            )  # nosec assert_used
            query = f"SELECT * FROM {self.table_names[0]}"  # nosec hardcoded_sql_expressions # noqa: B950
            data = pd.read_sql_query(
                sql=query,
                con=self.con,
            )
        return data

    @auto_validate
    def get_dtypes(self, table_name: Optional[str] = None, **kwargs: Any) -> _Dtypes:
        """Loads and returns the columns and column types from the Database dataset.

        Args:
            table_name: The name of the table_name which should be loaded. Only
                required for multitable database.

        Returns:
            A mapping from column names to column types.

        Raises:
            ValueError: If the data is multi-table but no table name provided.
        """
        metadata = MetaData(self.con)
        dtypes: _Dtypes
        if self.query is not None:
            with Session(self.con) as session:
                result = session.execute(text(self.query)).first()
            data = pd.DataFrame([result])
            dtypes = self._get_data_dtypes(data)

        elif table_name is not None:
            self._validate_table_name(table_name)

            table = Table(
                table_name,
                metadata,
                schema=self.db_conn.db_schema,
                autoload=True,
                autoload_with=self.con,
            )
            dtypes = {
                col.name: _convert_python_dtypes_to_pandas_dtypes(
                    col.type.python_type, col.name
                )
                for col in table.columns
            }
        else:
            raise ValueError("No table name provided for multi-table datasource.")
        return dtypes

    @auto_validate
    def yield_data(
        self, query: Optional[str] = None, **kwargs: Any
    ) -> Iterator[pd.DataFrame]:
        """Yields data from the database in partitions from the provided query.

        If query is not provided, the query from the datastructure is used.

        Args:
            query: An optional query to use for yielding data. Otherwise the query
                from the datastructure is used. A `query` is always provided when this
                method is called from the Dataset as part of a task.

        Raises:
            ValueError: If no query is provided and the datastructure has no query
                either.
        """
        query = query if query else self.query
        if query is None:
            raise ValueError("No query or table name specified.")

        with self.con.connect() as con:
            result = con.execute(text(query))
            for partition in result.partitions(self.partition_size):
                yield pd.DataFrame(partition, columns=list(result.keys()))
