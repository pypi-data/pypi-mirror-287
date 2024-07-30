from abc import ABC, abstractmethod
from uuid import UUID
from typing import TypeVar, Generic
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.entity import Entity
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.aggregate import Aggregate

T = TypeVar('T', bound=Entity)
U = TypeVar('U')
V = TypeVar('V')

class Aggregate(ABC):
    def __init__(self, root: Entity, id: UUID):
        self.root = root
        self.id = id

class AggregateWithState(Aggregate, Generic[T, U, V]):
    def __init__(self, root: T, id: UUID, state: U):
        super().__init__(root, id)
        self.state = state

    def change_state_to(self, new_state: V):
        new_state.handle(self)
        self.state = new_state



class BaseState(ABC):
    def __init__(self, state_enum):
        self.state_enum = state_enum

    @abstractmethod
    def handle(self, aggregate):
        pass

    def __str__(self):
        return self.state_enum.name.replace("State", "")


class IBaseState(ABC):
    @property
    @abstractmethod
    def state_enum(self):
        pass

    @abstractmethod
    def handle(self, aggregate):
        pass
