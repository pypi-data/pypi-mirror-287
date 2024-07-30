from abc import ABC, abstractmethod
from uuid import UUID

class IManageDomainEvents(ABC):
    
    def __init__(self):
        self._domain_events = {}
        
    @property
    def domain_events(self):
        return self._domain_events

    def pull_domain_events(self):
        events = list(self._domain_events.values())
        self._domain_events.clear()
        return events

    def pull_domain_events_by_type(self, event_type: type):
        events = [event for event in self._domain_events.values() if isinstance(event, event_type)]
        for event in events:
            self._domain_events.pop(event.id, None)
        return events

    def attach_event_stream(self, event_stream) -> None:
        # Implementar lógica para adjuntar el stream de eventos
        pass

    async def process_event_async(self, event_item) -> None:
        # Implementar lógica para procesar el evento de manera asíncrona
        pass

class IAggregate(IManageDomainEvents, ABC):
    
    @property
    @abstractmethod
    def id(self) -> UUID:
        pass

    @id.setter
    @abstractmethod
    def id(self, value: UUID) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
