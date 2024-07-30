from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID
import json
from abc import ABC, abstractmethod

from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects import IAggregate
from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent
from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate

@dataclass
class RolesUpdated:
    previous_roles: List[UUID]
    new_roles: List[UUID]

class ExampleRolesChanged(DomainEvent):
    def __init__(self, user=None, previous_ids=None, user_request=None):
        super().__init__(user_request)
        if user and previous_ids:
            user_registered = RolesUpdated(previous_ids, user.roles)
            self.j_data = json.dumps(user_registered, default=lambda o: str(o) if isinstance(o, UUID) else o.__dict__)

    async def handle(self, aggregate: IAggregate):
        if isinstance(self.source_aggregate_root, ExampleAggregate):
            example_agg = self.source_aggregate_root
            # Run some code with the handle
