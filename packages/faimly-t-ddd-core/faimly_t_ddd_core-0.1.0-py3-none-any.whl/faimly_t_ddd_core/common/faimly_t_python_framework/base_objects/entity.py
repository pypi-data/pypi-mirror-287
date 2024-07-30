from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass, field
import json

# Definimos un tipo genérico para el identificador
TId = TypeVar('TId')

@dataclass
class IEntity(ABC):
    @property
    @abstractmethod
    def id(self) -> Optional[object]:
        """
        The identifier of the entity.
        """
        pass

    @id.setter
    @abstractmethod
    def id(self, value: Optional[object]):
        pass

class Entity(ABC, Generic[TId]):
    id: Optional[TId] = field(default=None, repr=False)

    def __init__(self, id: Optional[TId] = None):
        if id is None:
            raise ValueError("id cannot be None")
        self.id = id

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Entity):
            return self.id == other.id
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        if self.id is None:
            raise ValueError("Cannot hash an entity with a None id")
        return hash(self.id)
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id})"

# Uso de la biblioteca json para la serialización
def to_json(entity: Entity) -> str:
    return json.dumps(entity, default=lambda o: o.__dict__)

def from_json(data: str, cls: type) -> Entity:
    data_dict = json.loads(data)
    return cls(**data_dict)
