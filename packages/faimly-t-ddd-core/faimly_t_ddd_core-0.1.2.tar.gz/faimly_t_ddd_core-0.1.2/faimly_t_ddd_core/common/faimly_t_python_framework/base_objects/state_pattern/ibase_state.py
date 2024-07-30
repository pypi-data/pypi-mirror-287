from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IBaseState(ABC, Generic[T]):
    @property
    @abstractmethod
    def state_enum(self) -> T:
        pass

    @abstractmethod
    def handle(self, aggregate: T) -> None:
        pass
