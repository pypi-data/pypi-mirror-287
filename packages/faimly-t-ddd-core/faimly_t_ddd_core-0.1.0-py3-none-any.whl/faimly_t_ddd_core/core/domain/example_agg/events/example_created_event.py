from typing import List, Optional
from uuid import UUID
import json
from dataclasses import dataclass

from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate
from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent
from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate

class ExampleCreatedEvent(DomainEvent):
    
    def __init__(self):
        self.j_data = None
        
    def handle(self, aggregate: ExampleAggregate):
        if isinstance(aggregate, ExampleAggregate):
            # Run some code with the handle
            user_registered = NewCreated(
                user_id_b2c=aggregate.id,
                email=aggregate.user.contact_information.email,
                name=aggregate.user.contact_information.name,
                roles_assigned=aggregate.roles
            )
            self.j_data = json.dumps(user_registered.to_dict())


@dataclass
class NewCreated:
    user_id_b2c: UUID
    email: str
    name: str
    roles_assigned: Optional[List[UUID]] = None

    def to_dict(self) -> dict:
        return {
            "userIdB2C": str(self.user_id_b2c),
            "email": self.email,
            "name": self.name,
            "rolesAssigned": [str(role) for role in self.roles_assigned] if self.roles_assigned else []
        }
