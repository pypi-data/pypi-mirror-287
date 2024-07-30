from abc import ABC, abstractmethod
from typing import List, Optional

from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.aggregate import IAggregate
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.aggregate import EventStream


class IEventRepository(ABC):
    @abstractmethod
    async def save_async(self, aggregate: IAggregate):
        pass

    @abstractmethod
    async def get_by_aggregate(self, aggregate_id: IAggregate) -> EventStream:
        pass

    @abstractmethod
    async def get_by_aggregates(self, aggregate_ids: List[IAggregate]) -> Optional[List[EventStream]]:
        pass
