import enum
from typing import List, Optional

from pydantic import BaseModel

from faimly_t_ddd_core.core.domain.example_agg.value_objects.example_associated_company import ExampleAssociatedCompany

# Define los estados asociados
class TypeAssociated(enum.Enum):
    Carrier = "Carrier"
    YardOwner = "YardOwner"

# Define los estados del usuario
class UserState(enum.Enum):
    Created = "Created"
    Approved = "Approved"

# Define las clases de ejemplo para los agregados y DTOs
class AssociatedCompanyDTO(BaseModel):
    Type: str
    ScacCode: str

    def __init__(self, pCompanyToTransform: Optional['ExampleAssociatedCompany'] = None, **data):
        super().__init__(**data)
        if pCompanyToTransform:
            self.Type = pCompanyToTransform.Type
            self.ScacCode = pCompanyToTransform.ScacCode

class ExampleAggDTO(BaseModel):
    User: 'ExampleUser'
    AssociatedCompanyId: AssociatedCompanyDTO
    RoleIds: List[str]  # Usando str en lugar de Guid
    StatusUser: str

    @property
    def ScacOwner(self) -> str:
        return self.AssociatedCompanyId.ScacCode

    @property
    def PartitionKey(self) -> str:
        return self.ScacOwner

    def MappingAggregate(self, aggregate: 'UserExampleAggregate'):
        self.User = aggregate.User
        self.StatusUser = aggregate.State.StateEnum.name
        self.RoleIds = aggregate.Roles
        self.AssociatedCompanyId = AssociatedCompanyDTO(pCompanyToTransform=aggregate.AssociatedCompanyId)

    def ToAggregate(self) -> 'UserExampleAggregate':
        builder = UserExampleAggregate.Builder.FromDTO(self.User, self.RoleIds, self.id)

        associated_company_type = TypeAssociated[self.AssociatedCompanyId.Type]

        if associated_company_type == TypeAssociated.Carrier:
            builder.WithAssociatedEntity(AssociatedCarrierCompany(self.AssociatedCompanyId.ScacCode))
        elif associated_company_type == TypeAssociated.YardOwner:
            builder.WithAssociatedEntity(AssociatedYardOwnerCompany(self.AssociatedCompanyId.ScacCode))
        else:
            raise ValueError(f"The user: {self.User.ContactInformation.Name}, from the database has an invalid Associated Company Type")

        if self.StatusUser == "Created":
            builder.WithState(ExampleCreatedState())
        elif self.StatusUser == "Approved":
            builder.WithState(ExampleAuthorizeState())
        
        return builder.Build()

# Define las clases asociadas a los estados y entidades (debe ser implementado según el caso)
class ExampleUser(BaseModel):
    pass

class UserExampleAggregate(BaseModel):
    class Builder:
        @staticmethod
        def FromDTO(user, role_ids, id):
            # Implementar método de construcción
            pass
        
        def WithAssociatedEntity(self, entity):
            # Implementar método para asociar entidad
            pass

        def WithState(self, state):
            # Implementar método para establecer estado
            pass
        
        def Build(self):
            # Implementar método para construir el agregado
            pass

class AssociatedCarrierCompany(BaseModel):
    pass

class AssociatedYardOwnerCompany(BaseModel):
    pass

class ExampleCreatedState(BaseModel):
    pass

class ExampleAuthorizeState(BaseModel):
    pass
