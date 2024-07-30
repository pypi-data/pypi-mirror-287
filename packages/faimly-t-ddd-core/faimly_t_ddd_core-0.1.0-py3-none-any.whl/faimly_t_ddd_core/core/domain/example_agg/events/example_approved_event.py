from dataclasses import dataclass
import json
from typing import List, Optional
from uuid import UUID
from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent
from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate

def custom_serializer(obj):
    if isinstance(obj, UUID):
        return str(obj)  # Convert UUID to string
    elif hasattr(obj, "__dict__"):
        return obj.__dict__  # Convert object with __dict__ attribute to dictionary
    raise TypeError(f"Type {type(obj)} not serializable")

class ExampleApprovedEvent(DomainEvent):
    def __init__(self, user: str):
        self.j_data = None
        super().__init__(user)

    def handle(self, aggregate: ExampleAggregate):
        if isinstance(aggregate, ExampleAggregate):
            user_registered = UserIsApproved(
                aggregate.id,
                aggregate.user.contact_information.email,
                aggregate.roles
            )

            self.j_data = json.dumps(user_registered, default=custom_serializer)

@dataclass
class UserIsApproved:
    user_id_b2c: str
    email: str
    roles_assigned: Optional[List[str]] = None