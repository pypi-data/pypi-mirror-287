from azure.cosmos import CosmosClient
from pydantic import BaseModel
import logging

from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.cosmos_db_config import CosmosDbConfig

class CosmosDbFacade:
    def __init__(self, config: CosmosDbConfig):
        try:
            self.client = CosmosClient(
                config.ConnectionString,
                consistency_level="Session"
            )
            self.database = self.client.get_database_client(config.DatabaseName)
            self.container = self.database.get_container_client(config.Container)
        except Exception as ex:
            logging.error(f"Error initializing Cosmos DB: {ex}")
            raise Exception(f"System cannot create the Database {config.DatabaseName}.")
