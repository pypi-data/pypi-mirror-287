from abc import ABC
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.state_pattern.ibase_state import IBaseState
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_states import ExampleState

class ExampleIState(IBaseState[ExampleState], ABC):
    pass
