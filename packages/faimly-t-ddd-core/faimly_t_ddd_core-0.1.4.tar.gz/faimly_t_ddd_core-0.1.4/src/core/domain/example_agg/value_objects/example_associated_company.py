from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class ExampleAssociatedCompany:
    type: str
    scac_code: str


class TypeAssociated(Enum):
    YARD_OWNER = "YardOwner"
    CARRIER = "Carrier"


@dataclass(frozen=True)
class AssociatedCarrierCompany(ExampleAssociatedCompany):
    scac_code: str

    def __init__(self, scac_code: str):
        super().__init__(TypeAssociated.CARRIER.value, scac_code)

@dataclass(frozen=True)
class AssociatedYardOwnerCompany(ExampleAssociatedCompany):
    scac_code: str

    def __init__(self, scac_code: str):
        super().__init__(TypeAssociated.YARD_OWNER.value, scac_code)
