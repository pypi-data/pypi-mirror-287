from abc import ABC, abstractmethod
from typing import Callable, TypeVar, Generic

from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate

TAggregate = TypeVar('TAggregate', bound='IAggregate')


class ISpecification(ABC, Generic[TAggregate]):
    @property
    @abstractmethod
    def where_criteria(self) -> Callable[[TAggregate], bool]:
        pass

    @property
    @abstractmethod
    def where_criteria_str(self) -> str:
        pass


class ISpecificationSingleOrDefault(ISpecification[TAggregate], ABC):
    pass


class ISpecificationToList(ISpecification[TAggregate], ABC):
    pass
