from typing import Callable
from pydantic import BaseModel, Field
from uuid import UUID

from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate

class ExampleGetByScacOwnerSpecification(BaseModel):
    where_criteria: Callable[[ExampleAggregate], bool]
    where_criteria_str: str

    @classmethod
    def from_scac_code(cls, p_scac_code_owner: str):
        where_criteria = lambda agg: agg.associated_company_id.scac_code == p_scac_code_owner

        if p_scac_code_owner == "SNEA":
            where_criteria_str = "c.ScacOwner IS NOT NULL"
        else:
            where_criteria_str = f"c.AssociatedCompanyId.ScacCode = '{p_scac_code_owner}'"

        return cls(where_criteria=where_criteria, where_criteria_str=where_criteria_str)

