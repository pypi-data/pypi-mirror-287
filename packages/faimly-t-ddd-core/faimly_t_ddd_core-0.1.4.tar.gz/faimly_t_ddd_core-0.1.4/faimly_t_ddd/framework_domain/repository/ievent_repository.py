from abc import ABC, abstractmethod
from typing import List, Optional

from faimly_t_ddd.framework_domain.base_objects.aggregate import EventStream, IAggregate



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
