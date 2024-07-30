from abc import ABC, abstractmethod
from typing import Type, TypeVar, Generic, List
import asyncio

from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.idomain_event_subscriber import DomainEventSubscriberBase

TEvent = TypeVar('TEvent', bound='DomainEvent')


class DomainEvent:
    pass


class Aggregate:
    def pull_domain_events(self) -> List[DomainEvent]:
        pass

    def pull_domain_events_typed(self, event_type: Type[TEvent]) -> List[TEvent]:
        pass


class IDomainEventPublisher(ABC):
    @abstractmethod
    async def publish_async(self, *aggregates: Aggregate):
        pass

    @abstractmethod
    async def publish_typed_async(self, event_type: Type[TEvent], *aggregates: Aggregate):
        pass

    @abstractmethod
    async def subscribe(self, *subscribers: DomainEventSubscriberBase):
        pass
