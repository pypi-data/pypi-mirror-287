from abc import ABC, abstractmethod
from typing import Dict, Generic, List, Type, TypeVar, Optional
from dataclasses import dataclass, field
import uuid
import asyncio

from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent

# Definimos un tipo genérico para eventos y entidades
TEvent = TypeVar('TEvent', bound='DomainEvent')
TEntityRoot = TypeVar('TEntityRoot', bound='IEntity')

@dataclass
class EventStream:
    pending_events: Dict[int, DomainEvent] = field(default_factory=dict)
    aggregate_events: Dict[int, DomainEvent] = field(default_factory=dict)
    id_aggregate: uuid.UUID = field(default_factory=uuid.uuid4)

    @property
    def current_version(self) -> int:
        return len(self.aggregate_events) + len(self.pending_events)

    def pull_pending_events(self) -> List[DomainEvent]:
        ordered_events = sorted(self.pending_events.items(), key=lambda e: e[0])
        pending_events_list = [e[1] for e in ordered_events]

        for key, event in ordered_events:
            self.aggregate_events[key] = event

        self.pending_events.clear()

        return pending_events_list

    def add_event(self, event: DomainEvent):
        self.pending_events[self.current_version + 1] = event

    def pull_domain_events(self, event_type: Type[TEvent]) -> List[TEvent]:
        selected_pending = {
            key: event for key, event in self.pending_events.items()
            if isinstance(event, event_type)
        }

        for key, event in selected_pending.items():
            self.aggregate_events[key] = event
            del self.pending_events[key]

        return list(selected_pending.values())

    def get_domain_events(self, event_type: Type[TEvent]) -> List[TEvent]:
        selected_pending = {
            key: event for key, event in self.pending_events.items()
            if isinstance(event, event_type)
        }

        aggregate_events = {
            key: event for key, event in self.aggregate_events.items()
            if isinstance(event, event_type)
        }

        domain_events = list(selected_pending.values()) + list(aggregate_events.values())
        return [event for event in domain_events if isinstance(event, event_type)]

class IEntity(ABC):
    @property
    @abstractmethod
    def id(self) -> Optional[uuid.UUID]:
        pass

    @id.setter
    @abstractmethod
    def id(self, value: Optional[uuid.UUID]):
        pass

class Aggregate(ABC, Generic[TEntityRoot]):
    root: TEntityRoot
    aggregate_event_stream: EventStream
    id: uuid.UUID

    def __init__(self, root: TEntityRoot, id: Optional[uuid.UUID] = None):
        if root is None:
            raise ValueError("root cannot be None")
        self.root = root
        self.id = id or uuid.uuid4()
        self.aggregate_event_stream = EventStream(id_aggregate=self.id)

    def attach_event_stream(self, event_stream: EventStream):
        if len(self.aggregate_event_stream.aggregate_events) > 0:
            raise ValueError("You can't assign an EventStream and replace an existing EventStream")
        self.aggregate_event_stream = event_stream

    def process_event_async(self, event_item: DomainEvent):
        try:
            event_item.handle(self)
            self.aggregate_event_stream.add_event(event_item)
        except Exception as ex:
            # Optionally, handle the exception or log it
            raise ex

    def pull_domain_events(self) -> List[DomainEvent]:
        if len(self.aggregate_event_stream.pending_events) > 0:
            return self.aggregate_event_stream.pull_pending_events()
        return []

    def pull_domain_events_by_type(self, event_type: Type[TEvent]) -> List[TEvent]:
        return self.aggregate_event_stream.pull_domain_events(event_type)

    def get_domain_events(self, event_type: Type[TEvent]) -> List[TEvent]:
        return self.aggregate_event_stream.get_domain_events(event_type)

    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def domain_events(self) -> List[DomainEvent]:
        # Combina eventos pendientes y agregados
        return list(self.aggregate_event_stream.pending_events.values()) + \
               list(self.aggregate_event_stream.aggregate_events.values())
