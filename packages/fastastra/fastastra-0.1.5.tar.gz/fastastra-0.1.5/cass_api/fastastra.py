from typing import Dict, Tuple, Any, Optional, List

from pydantic import BaseModel, create_model, Field

from cass_api.assistant.ddl_tool import DDLModel, Column
from datastore.providers.cassandra_datastore import CassandraDataStore
from datastore.providers.cassandra_util import get_pydantic_type, python_to_cassandra

class LoginPayload(BaseModel):
    db_id: str

datastores = {}

def get_datastore_from_cache(token) -> CassandraDataStore:
    global datastores
    if token in datastores:
        return datastores[token]
    raise Exception(detail="Must login to a database first")

def db_login(payload: LoginPayload, token: str):
    global datastores
    datastore = datastores.get(token)
    if datastore is None:
        datastore = CassandraDataStore()
    if payload.db_id == "":
        return Exception(detail='{"msg": "db_id is required."}')
    datastore.setupSession(token, payload.db_id)
    datastores[token] = datastore


class Table:
    def __init__(self, db, table_name):
        self.db = db
        self.table_name = table_name
        self.keyspace = db.keyspace
        self.columns = db.table_columns(table_name)

        model_name = ''.join(word.capitalize() for word in self.keyspace.split('_'))
        model_name += ''.join(word.capitalize() for word in self.table_name.split('_'))
        model_name += "Model"

        columns = self.db.client.get_columns(self.keyspace, self.table_name)
        model_fields: Dict[str, Tuple[Any, Any]] = {}
        for col in columns:
            if col['kind'] != 'partition_key' and col['kind'] != 'clustering':
                model_fields[col["column_name"]] = (Optional[get_pydantic_type(col["type"])], None)
            else:
                model_fields[col["column_name"]] = (get_pydantic_type(col["type"]), ...)

        ResponseModel = create_model(model_name, **model_fields)
        self.model = ResponseModel

    def exists(self) -> bool:
        tables = self.db.client.get_tables(self.keyspace)
        return self.table_name in tables

    def __repr__(self) -> str:
        return "<Table {}{}>".format(
            self.table_name,
            (
                " (does not exist yet)"
                if not self.exists()
                else " ({})".format(", ".join(c for c in self.columns))
            ),
        )

    def all(self) -> List[BaseModel]:
        rows = self.db.client.select_all_from_table(self.keyspace, self.table_name)
        return [self.model(**row) for row in rows]

    def create(
            self,
            partition_key: List[str] = None,
            clustering_columns: List[str] = None,
            columns: Dict[str, Any] = None,
            **kwargs
    ):
        if not columns:
            columns={}
        columns = {**columns, **kwargs}
        column_list = []
        if not partition_key:
            partition_key = []
        if isinstance(partition_key, str):
            partition_key = [partition_key]
        if not clustering_columns:
            clustering_columns = []
        if isinstance(clustering_columns, str):
            clustering_columns = [clustering_columns]
        for column_name, column_type in columns.items():
            column_list.append(Column(name=column_name, type=python_to_cassandra(column_type)))
        ddl_model = DDLModel(
            keyspace_name=self.db.keyspace,
            table_name=self.table_name,
            columns=column_list,
            partition_key=partition_key,
            clustering_columns=clustering_columns,
            thoughts=None
        )
        self.db.client.execute(ddl_model.to_string())
        self.columns = self.db.table_columns(self.table_name)

    @property
    def c(self):
        rows = self.db.client.get_columns(self.keyspace, self.table_name)
        return rows

    def insert(self, request_object: BaseModel = None, **kwargs):
        if request_object is None:
            request_object = self.model(**kwargs)
        self.db.client.upsert_table_from_dict(self.keyspace, self.table_name, request_object.dict())

    def update(self, request_object: BaseModel = None, **kwargs):
        self.insert(request_object, **kwargs)


class DynamicTables:
    def __init__(self, db, tables):
        self.db = db
        self._tables = tables

    def __getattr__(self, table_name) -> Table:
        for table in self._tables:
            if table.table_name == table_name:
                return table
        table = Table(self.db, table_name)
        return table

    def __dir__(self):
        table_names = []
        for table in self._tables:
            table_names.append(table.table_name)
        return self.db.client.get_tables(self.db.keyspace) + table_names


class Database:
    def __init__(self, token, dbid):
        login_payload = LoginPayload(db_id=dbid)
        db_login(login_payload, token)
        datastore = get_datastore_from_cache(token)
        self.client = datastore.client
        self.keyspace = "default_keyspace"
        self._tables = None

    def __del__(self):
        pass

    @property
    def t(self):
        if self._tables is None:
            rows = self.client.get_tables(self.keyspace)
            tables = []
            for row in rows:
                tables.append(row)
            self._tables = [Table(self, table) for table in tables]
        return self._tables

    @property
    def dt(self) -> DynamicTables:
        return DynamicTables(self, self.t)

    def table_columns(self, table_name):
        rows = self.client.get_columns(self.keyspace, table_name)
        columns = []
        for row in rows:
            columns.append(row["column_name"])
        return columns

