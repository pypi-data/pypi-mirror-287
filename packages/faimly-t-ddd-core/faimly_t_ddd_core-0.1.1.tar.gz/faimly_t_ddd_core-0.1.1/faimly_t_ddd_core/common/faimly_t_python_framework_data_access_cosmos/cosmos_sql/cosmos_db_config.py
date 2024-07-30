from dataclasses import dataclass

@dataclass
class CosmosDbConfig:
    connection_string: str
    database_name: str
    container: str
    partition_key_path: str
