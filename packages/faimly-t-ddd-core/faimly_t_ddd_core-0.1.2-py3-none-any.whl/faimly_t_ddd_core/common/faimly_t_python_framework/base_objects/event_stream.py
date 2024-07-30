from typing import Dict, List, Type, TypeVar, Union
from dataclasses import dataclass, field
import uuid

from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent

TEvent = TypeVar('TEvent', bound=DomainEvent)

@dataclass
class EventStream:
    pending_events: Dict[int, DomainEvent] = field(default_factory=dict)
    aggregate_events: Dict[int, DomainEvent] = field(default_factory=dict)
    id_aggregate: uuid.UUID = field(default_factory=uuid.uuid4)
    
    @property
    def current_version(self) -> int:
        return len(self.aggregate_events) + len(self.pending_events)

    def __init__(self, id_aggregate: uuid.UUID):
        self.id_aggregate = id_aggregate
        self.pending_events = {}
        self.aggregate_events = {}

    def __init__(self, p_events_historical: Dict[int, DomainEvent], p_id_cosmos_aggregate: uuid.UUID):
        self.id_aggregate = p_id_cosmos_aggregate
        self.pending_events = {}
        self.aggregate_events = p_events_historical

    def pull_pending_events(self) -> List[DomainEvent]:
        # Order the events by key in ascending order
        ordered_events = sorted(self.pending_events.items(), key=lambda e: e[0])
        pending_events_list = [e[1] for e in ordered_events]
        
        # Attach the events to the aggregate events
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
