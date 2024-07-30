from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime

from faimly_t_ddd.framework_domain.base_objects.IAggregate import IAggregate

# Define una clase base abstracta para eventos de dominio
@dataclass
class DomainEvent(ABC):
    user: str
    j_data: Optional[dict] = field(default=None)
    source_aggregate_root: Optional['IAggregate'] = field(default=None)
    time_stamp: datetime = field(default_factory=datetime.utcnow)
    
    @property
    def event_type(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def handle(self, aggregate: 'IAggregate'):
        pass

class GenericDomainEvent(DomainEvent):
    def __init__(self, user: str, j_data: Optional[dict] = None):
        super().__init__(user, j_data=j_data)
    
    async def handle(self, aggregate: 'IAggregate'):
        # Implementar la lógica específica para GenericDomainEvent si es necesario
        raise NotImplementedError("Handle method not implemented for GenericDomainEvent")
