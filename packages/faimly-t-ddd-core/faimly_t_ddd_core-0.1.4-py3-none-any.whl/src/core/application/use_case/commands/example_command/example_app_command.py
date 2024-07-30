from dataclasses import dataclass
import uuid

from src.core.domain.example_agg.example_aggregate import ExampleAggregate
from src.core.domain.repositories.i_example_repository import IExampleRepository

# Define the CommandExample equivalent
@dataclass
class CommandExample:
    field_id: int
    field_aggregate: int
    field_value_object: str
    p_user: str

@dataclass
class ResponseExample:
    p_new_transaction_id: uuid.UUID


# Define the command handler
class ExampleApplicationCommandHandler:
    def __init__(self, example_repository: IExampleRepository):
        self.example_repository = example_repository

    async def handle(self, command: CommandExample) -> ResponseExample:
        # Build/Get Aggregate and apply the domain logic as an example build the aggregate
        aggregate = ExampleAggregate.builder().build()

        await self.example_repository.save_async(aggregate)

        return ResponseExample(p_new_transaction_id=aggregate.id)

