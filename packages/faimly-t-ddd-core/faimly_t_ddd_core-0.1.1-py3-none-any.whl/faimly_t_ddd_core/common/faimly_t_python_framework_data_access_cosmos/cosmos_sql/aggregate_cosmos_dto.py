from pydantic import BaseModel, Field
from typing import Optional, TypeVar, Generic
from datetime import datetime
import uuid

from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.iaggregate_dto import IAggregateDTO


TAggregate = TypeVar('TAggregate', bound=IAggregate)

class AggregateCosmosDTO(BaseModel, IAggregateDTO[TAggregate], Generic[TAggregate]):
    _aggregate: Optional[TAggregate] = None
    Ts: int = Field(..., alias='_ts')
    idCosmos: str = Field(..., alias='id')
    _rid: str
    _self: str
    _etag: str = Field(..., alias='_etag')
    _attachments: str
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    class Config:
        allow_population_by_field_name = True

    @property
    def TimeStampUtc(self) -> datetime:
        return datetime.utcfromtimestamp(self.Ts)

    @property
    def PartitionKey(self) -> str:
        raise NotImplementedError

    def GetDTOFromEntity(self, pEntity: TAggregate):
        self._aggregate = pEntity
        self.idCosmos = str(self._aggregate.Id)
        self.MappingAggregate()

    def ToAggregate(self) -> TAggregate:
        raise NotImplementedError

    def MappingAggregate(self):
        raise NotImplementedError

    def __init__(self, **data):
        super().__init__(**data)
        if self.idCosmos:
            self.id = uuid.UUID(self.idCosmos)
