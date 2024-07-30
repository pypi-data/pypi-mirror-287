from faimly_t_ddd.framework_data_access.cosmos_sql.configurations_helper import ConfigurationsHelper
from faimly_t_ddd.framework_data_access.cosmos_sql.cosmos_collection_repository import CosmosCollectionRepository
from src.core.domain.repositories.i_example_repository import IExampleRepository
from src.infrastructure.data_access.dto.example_agg_dto import ExampleAggDTO, UserExampleAggregate
from src.infrastructure.data_access.repository.example_event_repository import ExampleEventsRepository

class ExampleRepository(
    CosmosCollectionRepository[UserExampleAggregate, ExampleAggDTO],
    IExampleRepository
):
    def __init__(
        self,
        p_event_repository: 'ExampleEventsRepository'
    ) -> None:
        cosmos_config = ConfigurationsHelper("ExampleDBCosmos").get_cosmos_configuration("ConnectionStrings__CosmosAccountConnStr", "ExampleDBCosmos")
        super().__init__(cosmos_config, p_event_repository)
