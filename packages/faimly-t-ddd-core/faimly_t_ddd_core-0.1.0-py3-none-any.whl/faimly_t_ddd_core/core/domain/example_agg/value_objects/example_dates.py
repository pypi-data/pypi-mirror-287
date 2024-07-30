from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class ExampleDates:
    created_at: datetime = field(default_factory=lambda: datetime.utcnow())
    updated_at: datetime = field(default_factory=lambda: datetime.utcnow())

    def __init__(self, created_at=None, updated_at=None):
        if created_at is None:
            created_at = datetime.utcnow()
        if updated_at is None:
            updated_at = datetime.utcnow()
        self.created_at = created_at
        self.updated_at = updated_at
