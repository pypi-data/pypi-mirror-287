from abc import ABC, abstractmethod
from typing import List, Generic, TypeVar, Optional
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate
from faimly_t_ddd_core.common.faimly_t_python_framework.repository.ispecification import ISpecificationSingleOrDefault, ISpecificationToList
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.iaggregate_dto import IAggregateDTO

TAggregate = TypeVar('TAggregate', bound='IAggregate')
TAggregateDTO = TypeVar('TAggregateDTO', bound=IAggregateDTO)

class ICollectionRepository(Generic[TAggregate, TAggregateDTO]):
    @abstractmethod
    async def save_async(self, aggregate: TAggregate):
        pass

    @abstractmethod
    async def save_all_async(self, aggregates_to_save: List[TAggregate]):
        pass

    @abstractmethod
    async def save_with_specification_async(
        self, entity_to_load: TAggregate, specification_find: ISpecificationSingleOrDefault[TAggregate]
    ) -> TAggregate:
        pass

    @abstractmethod
    async def get_by_specification_async(
        self, specification_where: ISpecificationToList[TAggregate], include_events: bool = True
    ) -> List[Optional[TAggregate]]:
        pass

    @abstractmethod
    async def get_single_by_specification_async(
        self, specification_where: ISpecificationSingleOrDefault[TAggregate], include_events: bool = True
    ) -> Optional[TAggregate]:
        pass

    @abstractmethod
    async def get_all_async(self) -> List[TAggregate]:
        pass

    @abstractmethod
    async def delete_async(self, aggregate: TAggregate) -> TAggregate:
        pass
