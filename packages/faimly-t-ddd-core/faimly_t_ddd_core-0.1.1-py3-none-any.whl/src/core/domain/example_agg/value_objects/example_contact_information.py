from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ExampleContactInformation:
    name: str
    email: str
    phone_number: Optional[int] = None
