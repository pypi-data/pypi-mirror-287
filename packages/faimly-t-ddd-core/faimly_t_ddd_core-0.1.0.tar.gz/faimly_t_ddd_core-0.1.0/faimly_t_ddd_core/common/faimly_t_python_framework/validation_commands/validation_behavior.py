from typing import Callable, TypeVar, Generic, List
from pydantic import BaseModel, ValidationError
from abc import ABC, abstractmethod

TRequest = TypeVar('TRequest', bound=BaseModel)
TResponse = TypeVar('TResponse')


class IPipelineBehavior(ABC, Generic[TRequest, TResponse]):
    @abstractmethod
    async def handle(self, request: TRequest, next: Callable[[], TResponse]):
        pass


class ValidationBehavior(IPipelineBehavior[TRequest, TResponse]):
    def __init__(self, validators: List[Callable[[TRequest], None]]):
        self._validators = validators

    async def handle(self, request: TRequest, next: Callable[[], TResponse]):
        if self._validators:
            errors = []
            for validator in self._validators:
                try:
                    validator(request)
                except ValidationError as e:
                    errors.extend(e.errors())

            if errors:
                if isinstance(next(), Result):
                    return Result(errors=errors, valid=False)
                else:
                    raise ValidationError(errors)

        return await next()


class Result(Generic[TResponse]):
    def __init__(self, data: TResponse = None, errors: List[str] = None, valid: bool = True):
        self.data = data
        self.errors = errors or []
        self.valid = valid

    @classmethod
    def invalid(cls, errors: List[str]):
        return cls(errors=errors, valid=False)
