from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from pydantic import ValidationError, BaseModel

T = TypeVar('T', bound=BaseModel)


class ISpecificationValidation(ABC, Generic[T]):
    @abstractmethod
    async def validate(self, command_to_validate: T) -> ValidationError:
        pass
