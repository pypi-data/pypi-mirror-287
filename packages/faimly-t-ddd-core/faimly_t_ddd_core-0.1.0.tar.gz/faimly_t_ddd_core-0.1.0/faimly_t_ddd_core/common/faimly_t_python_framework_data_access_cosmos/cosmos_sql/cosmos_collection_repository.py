import logging
from typing import Any, List, Optional, TypeVar, Generic
from fastapi import HTTPException
from azure.cosmos import CosmosClient, PartitionKey, exceptions as cosmos_exceptions
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate
from faimly_t_ddd_core.common.faimly_t_python_framework.repository.icollection_repository import ICollectionRepository
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.cosmos_db_config import CosmosDbConfig
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.iaggregate_dto import IAggregateDTO

TAggregate = TypeVar('TAggregate', bound=IAggregate)
TAggregateDTO = TypeVar('TAggregateDTO', bound=IAggregateDTO)

# class ExampleRepository(CosmosCollectionRepository):
#     def __init__():
#         super.__init__("ExampleDBCosmos", "EventsExampleDb")

class CosmosCollectionRepository(ICollectionRepository[TAggregate, TAggregateDTO]):
    def __init__(self, config: CosmosDbConfig, event_repository: Any):
        self.config = config
        self.event_repository = event_repository

        self.client = CosmosClient.from_connection_string(
            config.connection_string,
            consistency_level="Session"
        )

        self.database = self.client.get_database_client(config.database_name)
        self.container = self.database.get_container_client(config.container)

    async def save_async(self, aggregate: TAggregate):
        try:
            await self.event_repository.save_async(aggregate)

            entity_dto = TAggregateDTO()
            entity_dto.GetDTOFromEntity(aggregate)

            await self.container.upsert_item(
                item=entity_dto.dict(by_alias=True),
                partition_key=PartitionKey(entity_dto.PartitionKey)
            )
        except cosmos_exceptions.CosmosHttpResponseError as ex:
            logging.error(f"CosmosException saving the aggregate {aggregate} with {aggregate.Id}, "
                         f"and StatusCode {ex.status_code} - SubStatusCode {ex.sub_status_code}, "
                         f"and message {ex.message}")
            raise HTTPException(status_code=500, detail=f"Error saving the aggregate: {ex.message}")
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def get_by_specification_async(self, specification: str, include_events: bool = True) -> Optional[List[TAggregate]]:
        query = f"SELECT * FROM c WHERE {specification}"
        items = self.container.query_items(query=query, enable_cross_partition_query=True)

        results = []
        async for item in items:
            dto = TAggregateDTO(**item)
            aggregate = dto.ToAggregate()
            results.append(aggregate)

        if include_events:
            aggregates = [result for result in results if result is not None]
            event_streams = await self.event_repository.get_by_aggregate(aggregates)
            for result in results:
                event_stream = next((x for x in event_streams if x.IdAggregate == result.Id), None)
                if event_stream:
                    result.attach_event_stream(event_stream)

        return results

    async def delete_async(self, aggregate: TAggregate):
        try:
            await self.container.delete_item(
                item=aggregate.Id,
                partition_key=PartitionKey(aggregate.PartitionKey)
            )
        except cosmos_exceptions.CosmosHttpResponseError as ex:
            logging.error(f"CosmosException deleting the aggregate {aggregate} with {aggregate.Id}, "
                         f"and StatusCode {ex.status_code} - SubStatusCode {ex.sub_status_code}, "
                         f"and message {ex.message}")
            raise HTTPException(status_code=500, detail=f"Error deleting the aggregate: {ex.message}")
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))
