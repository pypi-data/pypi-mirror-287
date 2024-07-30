from abc import ABC
from faimly_t_ddd.framework_domain.base_objects.state_pattern.ibase_state import IBaseState
from src.core.domain.example_agg.value_objects.states.example_states import ExampleState

class ExampleIState(IBaseState[ExampleState], ABC):
    pass
