import inspect
from typing import Dict, Type, TypeVar

from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent, GenericDomainEvent


T = TypeVar('T', bound=Type[DomainEvent])

class DomainEventTypeResolver:
    EventTypes: Dict[str, Type[DomainEvent]] = {}

    @staticmethod
    def register_domain_event_types(reference_type: Type[T]):
        # Obtiene el módulo del tipo de referencia
        module = inspect.getmodule(reference_type)
        if module is None:
            raise ValueError("No se pudo obtener el módulo del tipo de referencia")

        # Obtiene todas las clases en el módulo que heredan de DomainEvent y no son abstractas
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, DomainEvent) and obj is not DomainEvent:
                DomainEventTypeResolver.EventTypes[obj.__name__] = obj

    @staticmethod
    def get_event_type(type_name: str) -> Type[DomainEvent]:
        return DomainEventTypeResolver.EventTypes.get(type_name, GenericDomainEvent)

