from collections import defaultdict
from typing import List, Type, TypeVar, Generic

from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent

TEvent = TypeVar('TEvent', bound='DomainEvent')


class Aggregate:
    def pull_domain_events(self) -> List[DomainEvent]:
        pass

    def pull_domain_events_typed(self, event_type: Type[TEvent]) -> List[TEvent]:
        pass


class DomainEventSubscriberBase(Generic[TEvent]):
    async def notify_event_async(self, domain_event: TEvent):
        pass


class DomainEventPublisher:
    def __init__(self):
        self._subscribers = defaultdict(list)

    async def subscribe(self, *subscribers: DomainEventSubscriberBase):
        for subscriber in subscribers:
            event_type = type(subscriber).__orig_bases__[0].__args__[0]
            self._subscribers[event_type].append(subscriber)

    async def publish_async(self, *aggregates: Aggregate):
        for aggregate in aggregates:
            for event_to_publish in aggregate.pull_domain_events():
                event_type = type(event_to_publish)
                if event_type in self._subscribers:
                    for handler in self._subscribers[event_type]:
                        await handler.notify_event_async(event_to_publish)

    async def publish_typed_async(self, event_type: Type[TEvent], *aggregates: Aggregate):
        for aggregate in aggregates:
            for event_to_publish in aggregate.pull_domain_events_typed(event_type):
                if event_type in self._subscribers:
                    for handler in self._subscribers[event_type]:
                        await handler.notify_event_async(event_to_publish)
