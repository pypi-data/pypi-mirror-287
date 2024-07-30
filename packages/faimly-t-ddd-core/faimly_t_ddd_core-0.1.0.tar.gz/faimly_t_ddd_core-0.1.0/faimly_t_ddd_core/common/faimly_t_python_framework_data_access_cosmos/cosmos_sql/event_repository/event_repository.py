from typing import List, Dict, Type, Optional
import uuid
from azure.cosmos import CosmosClient, PartitionKey, exceptions as cosmos_exceptions
from pydantic import BaseModel
import logging
import json

from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.aggregate import EventStream
from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.cosmos_db_config import CosmosDbConfig
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.event_repository.domain_event_converter import DomainEventTypeResolver

class DomainEventStoreAdapterCosmos(BaseModel):
    id_cosmos: str
    aggregate_name: str
    events: Optional[List[Dict]] = []

    @property
    def partition_key(self) -> str:
        return self.aggregate_name

    def return_event_stream(self, aggregate_type: Type[ExampleAggregate]) -> EventStream:
        DomainEventTypeResolver.register_domain_event_types(aggregate_type)

        result = {}
        if self.events:
            for event in self.events:
                event_type = event.get("EventType")
                type_ = DomainEventTypeResolver.get_event_type(event_type)
                if type_ is None:
                    raise ValueError(f"Unknown event type: {event_type}")

                domain_event = json.loads(json.dumps(event), object_hook=type_)
                sequence = event["sequence"]
                result[sequence] = domain_event

        try:
            id_guid = uuid.UUID(self.id_cosmos)
        except ValueError:
            id_guid = None

        return EventStream(result, id_guid)

class EventRepository:
    def __init__(self, config: CosmosDbConfig):
        self.client = CosmosClient.from_connection_string(config.connection_string)
        self.container = self.client.get_database_client(config.database_name).get_container_client(config.container)
        
    async def get_by_aggregate(self, aggregate: ExampleAggregate) -> Optional[EventStream]:
        try:
            query = f"SELECT * FROM c WHERE c.id = '{aggregate.id}'"
            items = list(self.container.query_items(query=query, enable_cross_partition_query=True))

            if items:
                item = items[0]
                adapter = DomainEventStoreAdapterCosmos(**item)
                return adapter.return_event_stream(type(aggregate))
            
            return None

        except cosmos_exceptions.CosmosHttpResponseError as ex:
            logging.error(f"CosmosException getting the aggregate Event Stream by Aggregate Id {aggregate.id}: {ex}")
            raise ex

        except Exception as ex:
            logging.error(f"Exception getting the aggregate Event Stream by Aggregate Id {aggregate.id}: {ex}")
            raise ex

    async def get_by_aggregates(self, aggregates: List[ExampleAggregate]) -> Optional[List[EventStream]]:
        try:
            aggregate_ids = "', '".join([agg.id for agg in aggregates])
            query = f"SELECT * FROM c WHERE c.id IN ('{aggregate_ids}')"
            items = list(self.container.query_items(query=query, enable_cross_partition_query=True))

            if items:
                event_streams = []
                for item in items:
                    adapter = DomainEventStoreAdapterCosmos(**item)
                    event_streams.append(adapter.return_event_stream(type(aggregates[0])))
                return event_streams

            return None

        except cosmos_exceptions.CosmosHttpResponseError as ex:
            logging.error(f"CosmosException getting the aggregate Event Stream by Aggregate Ids {aggregate_ids}: {ex}")
            raise ex

        except Exception as ex:
            logging.error(f"Exception getting the aggregate Event Stream by Aggregate Ids {aggregate_ids}: {ex}")
            raise ex

    async def save_async(self, aggregate: ExampleAggregate):
        try:
            entity = DomainEventStoreAdapterCosmos(
                id_cosmos=str(aggregate.id),
                aggregate_name=type(aggregate).__name__,
                events=[{
                    "sequence": index,
                    "User": event.user if hasattr(event, "user") else None,
                    "TimeStamp": event.time_stamp.isoformat() if hasattr(event, "time_stamp") else None,
                    "Data": event.j_data,
                    "EventType": event.event_type
                } for index, event in enumerate(aggregate.domain_events)]
            )
            await self.container.upsert_item(item=entity.dict(), partition_key=PartitionKey(entity.partition_key))

        except cosmos_exceptions.CosmosHttpResponseError as ex:
            logging.error(f"CosmosException saving the aggregate Event Stream {aggregate.domain_events} with Id {aggregate.id}: {ex}")
            raise ex

        except Exception as ex:
            logging.error(f"Exception saving the aggregate Event Stream {aggregate.domain_events} with Id {aggregate.id}: {ex}")
            raise ex
