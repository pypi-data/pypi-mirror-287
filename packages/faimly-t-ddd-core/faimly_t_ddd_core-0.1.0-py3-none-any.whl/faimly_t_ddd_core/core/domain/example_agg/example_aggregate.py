from typing import List, Optional, Iterable
from uuid import UUID
from dataclasses import dataclass, field
import asyncio

# Importando clases desde los módulos correspondientes
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.aggregate import Aggregate
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.state_pattern.aggregate_with_state import AggregateWithState
from faimly_t_ddd_core.core.domain.example_agg.entities.example import Example
from faimly_t_ddd_core.core.domain.example_agg.value_objects.example_associated_company import ExampleAssociatedCompany
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_i_user_state import ExampleIState
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_states import ExampleState


@dataclass
class ExampleAggregate(Aggregate[Example], AggregateWithState[Example, ExampleIState, ExampleState]):

    def __init__(self,
                 root: Example,
                 associated_company_id: ExampleAssociatedCompany,
                 roles: Optional[Iterable[UUID]] = None,
                 state: Optional[ExampleIState] = None):
        super().__init__(root, root.id)  # Llama al constructor de Aggregate
        AggregateWithState.__init__(self, root, root.id, state)  # Llama al constructor de AggregateWithState
        self.associated_company_id = associated_company_id
        self.roles = list(roles) if roles else []

        if state:
            self.state = state
            state.handle(self)


    def approved_user(self, user_approving: str):
        from faimly_t_ddd_core.core.domain.example_agg.events.example_approved_event import ExampleApprovedEvent
        self.process_event_async(ExampleApprovedEvent(user_approving))

    @property
    def user(self) -> Example:
        return self.root

    @staticmethod
    def builder():
        from faimly_t_ddd_core.core.domain.example_agg.factories.example_builder import ExampleBuilder
        return ExampleBuilder()
    
    # def process_event_async(self, event: DomainEvent):
    #     event.handle(self)
