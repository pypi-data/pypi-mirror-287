from dataclasses import dataclass, field
from uuid import UUID, uuid4
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.entity import Entity
from faimly_t_ddd_core.core.domain.example_agg.value_objects.example_contact_information import ExampleContactInformation

@dataclass
class Example(Entity[UUID]):
    contact_information: ExampleContactInformation = None
    url_avatar_img: str = None

    def __init__(self, id: UUID = None, contact_information: ExampleContactInformation = None, url_avatar_img: str = None):
        if id is None:
            id = uuid4()
        super().__init__(id)
        self.contact_information = contact_information
        self.url_avatar_img = url_avatar_img

    @classmethod
    def create_with_auto_id(cls, contact_information: ExampleContactInformation, url_avatar_img: str):
        return cls(uuid4(), contact_information, url_avatar_img)
