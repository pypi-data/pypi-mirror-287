from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ExampleAccessRights:
    resource: str
    has_access: bool
    full_access: bool
    permissions: Optional[List[str]] = None
