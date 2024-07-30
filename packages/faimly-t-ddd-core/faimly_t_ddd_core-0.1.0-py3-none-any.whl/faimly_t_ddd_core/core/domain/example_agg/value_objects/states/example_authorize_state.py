from typing import Optional

from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_i_user_state import ExampleIState
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_states import ExampleState

class ExampleAuthorizeState(ExampleIState):
    def __init__(self, user_approving: Optional[str] = None):
        self._user_approving = user_approving
        self.state_enum = ExampleState.APPROVED

    async def handle(self, aggregate: IAggregate):
        # if isinstance(aggregate, UserExampleAggregate):
        #     await aggregate.process_event_async(
        #         ExampleUserApprovedEvent(self._user_approving)
        #     )
        pass
