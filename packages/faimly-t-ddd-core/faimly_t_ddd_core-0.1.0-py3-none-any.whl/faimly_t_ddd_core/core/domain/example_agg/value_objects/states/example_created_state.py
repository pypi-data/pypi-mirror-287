from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate
from faimly_t_ddd_core.core.domain.example_agg.events.example_created_event import ExampleCreatedEvent
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_i_user_state import ExampleIState
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_states import ExampleState

class ExampleCreatedState(ExampleIState):
    @property
    def state_enum(self) -> ExampleState:
        return ExampleState.CREATED

    def handle(self, aggregate: IAggregate) -> None:
        aggregate.process_event_async(
            ExampleCreatedEvent()
        )
