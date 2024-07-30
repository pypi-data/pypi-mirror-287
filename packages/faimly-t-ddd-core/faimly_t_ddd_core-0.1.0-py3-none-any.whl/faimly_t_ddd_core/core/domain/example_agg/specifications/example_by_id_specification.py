from typing import Callable, Optional
from pydantic import BaseModel, Field, ValidationError, validator
from uuid import UUID

from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_states import ExampleState

class ExampleByIdSpecification(BaseModel):
    where_criteria: Callable[[ExampleAggregate], bool]
    where_criteria_str: str

    @classmethod
    def from_uuid(cls, user_aggregate_id: UUID):
        where_criteria = lambda agg: agg.id == user_aggregate_id
        where_criteria_str = f"c.id = '{user_aggregate_id}'"
        return cls(where_criteria=where_criteria, where_criteria_str=where_criteria_str)

    @classmethod
    def from_str(cls, user_aggregate_id: str):
        try:
            user_guid = UUID(user_aggregate_id)
        except ValueError:
            raise ValueError(f"To build the search by User Id the param should be a valid UUID: {user_aggregate_id}")

        where_criteria = lambda agg: agg.id == user_guid
        where_criteria_str = f"c.id = '{user_guid}'"
        return cls(where_criteria=where_criteria, where_criteria_str=where_criteria_str)

class ExampleApprovedByIdSpecification(ExampleByIdSpecification):
    @classmethod
    def from_uuid(cls, user_aggregate_id: UUID):
        where_criteria = lambda agg: agg.id == user_aggregate_id and agg.state and agg.state.state_enum == ExampleState.Approved
        where_criteria_str = f"c.id = '{user_aggregate_id}' and (c.StatusUser = '{ExampleState.Approved}' or c.StatusUser = '{ExampleState.Created}')"
        return cls(where_criteria=where_criteria, where_criteria_str=where_criteria_str)

