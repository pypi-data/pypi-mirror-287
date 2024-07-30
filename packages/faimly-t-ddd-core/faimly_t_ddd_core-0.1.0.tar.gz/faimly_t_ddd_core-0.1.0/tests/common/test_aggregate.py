import pytest
import uuid
from typing import Optional

from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.aggregate import Aggregate, EventStream
from faimly_t_ddd_core.common.faimly_t_python_framework.base_objects.entity import IEntity
from faimly_t_ddd_core.common.faimly_t_python_framework.domain_events.domain_event import DomainEvent, IAggregate

# Definimos una implementación básica de IEntity para pruebas
class MockEntityRoot(IEntity):
    def __init__(self, id: uuid.UUID):
        self._id = id

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, value: uuid.UUID):
        self._id = value

# Definimos un evento de dominio ficticio para pruebas
class MockDomainEvent(DomainEvent):
    async def handle(self, aggregate: IAggregate):
        # Implementar la lógica específica para el manejo del evento en pruebas
        pass

# Definimos una implementación de Aggregate para pruebas
class MockAggregate(Aggregate[MockEntityRoot]):
    def __init__(self, root: MockEntityRoot, id: Optional[uuid.UUID] = None):
        super().__init__(root, id)

@pytest.fixture
def setup_aggregate():
    root_entity = MockEntityRoot(uuid.uuid4())
    aggregate = MockAggregate(root_entity, root_entity.id)
    return aggregate

def test_aggregate_initialization(setup_aggregate):
    aggregate = setup_aggregate
    assert isinstance(aggregate, MockAggregate)
    assert aggregate.root is not None
    assert isinstance(aggregate.aggregate_event_stream, EventStream)
    assert aggregate.id == aggregate.aggregate_event_stream.id_aggregate

def test_add_event(setup_aggregate):
    aggregate = setup_aggregate
    event = MockDomainEvent(user='test_user')
    aggregate.aggregate_event_stream.add_event(event)
    assert len(aggregate.aggregate_event_stream.pending_events) == 1

def test_pull_domain_events(setup_aggregate):
    aggregate = setup_aggregate
    event = MockDomainEvent(user='test_user')
    aggregate.aggregate_event_stream.add_event(event)
    pulled_events = aggregate.pull_domain_events()
    assert len(pulled_events) == 1
    assert isinstance(pulled_events[0], DomainEvent)

def test_attach_event_stream(setup_aggregate):
    aggregate = setup_aggregate
    new_event_stream = EventStream(aggregate.id)
    aggregate.attach_event_stream(new_event_stream)
    assert aggregate.aggregate_event_stream == new_event_stream

@pytest.mark.asyncio
async def test_process_event_async(setup_aggregate):
    aggregate = setup_aggregate
    event = MockDomainEvent(user='test_user')
    aggregate.process_event_async(event)
    assert len(aggregate.aggregate_event_stream.pending_events) == 1
