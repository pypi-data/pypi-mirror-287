from faimly_t_ddd.framework_data_access.cosmos_sql.cosmos_db_config import CosmosDbConfig


class ExampleEventsDBCosmos(CosmosDbConfig):
    CONN_STRING = "ConnectionStrings__CosmosAccountConnStr"
    COSMOS_SECTION = "EventsExampleDb"
