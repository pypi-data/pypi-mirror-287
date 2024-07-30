from typing import Generic, TypeVar

from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate


TAggregate = TypeVar('TAggregate', bound=IAggregate)

class IAggregateDTO(Generic[TAggregate]):
    @property
    def PartitionKey(self) -> str:
        raise NotImplementedError

    def GetDTOFromEntity(self, pEntity: TAggregate):
        raise NotImplementedError

    def MappingAggregate(self):
        raise NotImplementedError

    def ToAggregate(self) -> TAggregate:
        raise NotImplementedError
