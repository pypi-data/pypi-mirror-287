import os
from pydantic import BaseModel
from fastapi import HTTPException

from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.cosmos_db_config import CosmosDbConfig

def get_env_variables(prefix: str) -> dict:
    env_vars = {}
    # Recorre todas las variables de entorno
    for key, value in os.environ.items():
        # Verifica si la clave comienza con el prefijo especificado
        if key.startswith(prefix) or key.startswith("ConnectionStrings__Cosmos"):
            # Agrega la variable al diccionario
            env_vars[key] = value

    return env_vars

class ConfigurationsHelper:

    def __init__(self, key_section: str):
        self.config = get_env_variables(key_section)
    
    def get_cosmos_configuration(self, key_connection: str, key_section: str) -> CosmosDbConfig:
        connection_string = self.config.get(key_connection)
        database_name = self.config.get(f"{key_section}__DatabaseName")
        container = self.config.get(f"{key_section}__Container")
        partition_key_path = self.config.get(f"{key_section}__PartitionKeyPath")

        if not connection_string:
            raise HTTPException(status_code=500, detail=f"Cannot load the connection string: {key_connection}")

        if not database_name:
            raise HTTPException(status_code=500, detail=f"Cannot load the database name: {key_section}")

        if not container:
            raise HTTPException(status_code=500, detail=f"Cannot load the container: {key_section}")

        if not partition_key_path:
            raise HTTPException(status_code=500, detail=f"Cannot load the partition key: {key_section}")

        return CosmosDbConfig(
            connection_string=connection_string,
            database_name=database_name,
            container=container,
            partition_key_path=partition_key_path
        )

    def get_connection_string(self, key_connection: str) -> str:
        connection_string = self.config.get(key_connection)
        if not connection_string:
            raise HTTPException(status_code=500, detail=f"Cannot load the connection string: {key_connection}")
        return connection_string
