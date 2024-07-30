from typing import Optional, List
from uuid import UUID
import uuid

from faimly_t_ddd_core.core.domain.example_agg.entities.example import Example

from faimly_t_ddd_core.core.domain.example_agg.value_objects.example_associated_company import ExampleAssociatedCompany
from faimly_t_ddd_core.core.domain.example_agg.value_objects.example_contact_information import ExampleContactInformation
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_created_state import ExampleCreatedState
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_i_user_state import ExampleIState

class ExampleBuilder:
    def __init__(self):
        self._user: Optional[Example] = None
        self._user_state: Optional[ExampleIState] = None
        self._associated_company: Optional[ExampleAssociatedCompany] = None
        self._roles: Optional[List[UUID]] = None

    def with_user(self, name: str, email: str, phone_number: Optional[int] = None, id: Optional[UUID] = None) -> 'ExampleBuilder':
        if id is None:
            id = uuid.uuid4()

        self._user = Example(id)
        self._user.contact_information = ExampleContactInformation(name, email, phone_number)
        return self

    def from_dto(self, user: Example, role_ids: Optional[List[UUID]], id_user: UUID) -> 'ExampleBuilder':
        self._user = Example(id_user)
        self._user.contact_information = user.contact_information
        self._user.url_avatar_img = user.url_avatar_img
        self._roles = role_ids
        return self

    def with_associated_entity(self, associated_company: ExampleAssociatedCompany) -> 'ExampleBuilder':
        self._associated_company = associated_company
        return self

    def with_state(self, user_state: ExampleIState) -> 'ExampleBuilder':
        self._user_state = user_state
        return self

    def build(self):
        from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate
        
        if self._user is None:
            raise ValueError("User must be specified.")

        if self._associated_company is None:
            raise ValueError("User must have an associated Company (Carrier or YardOwner)")

        if self._user_state is None:
            self._user_state = ExampleCreatedState(self._user)

        return ExampleAggregate(
            self._user,
            self._associated_company,
            self._roles,
            self._user_state
        )
