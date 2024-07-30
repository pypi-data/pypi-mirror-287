from typing import ClassVar
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.cosmos_db_config import CosmosDbConfig

class ExampleDBCosmos(CosmosDbConfig):
    CONN_STRING = "ConnectionStrings__CosmosAccountConnStr"
    COSMOS_SECTION = "ExampleDBCosmos"
