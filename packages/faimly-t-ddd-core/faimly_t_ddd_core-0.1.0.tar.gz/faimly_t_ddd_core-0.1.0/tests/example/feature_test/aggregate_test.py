import pytest

from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate
from faimly_t_ddd_core.core.domain.example_agg.value_objects.example_associated_company import AssociatedCarrierCompany, AssociatedYardOwnerCompany
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_created_state import ExampleCreatedState
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_states import ExampleState


@pytest.fixture
def setup_builder():
    def _setup_builder(name, email, phone_number, associated_company, user_state):
        builder = ExampleAggregate.builder() \
            .with_user(name, email, phone_number) \
            .with_associated_entity(associated_company) \
            .with_state(user_state)
        return builder
    return _setup_builder

def test_build_should_create_user_aggregate_with_valid_data(setup_builder):
    # Arrange
    builder = setup_builder(
        "Max Rodriguez",
        "mfrodriguez@snecorp.com",
        50377589833,
        AssociatedYardOwnerCompany("SNEA"),
        ExampleCreatedState()
    )
    
    # Act
    user_aggregate = builder.build()

    # Assert
    assert user_aggregate is not None
    assert user_aggregate.user.contact_information.name == "Max Rodriguez"
    assert user_aggregate.user.contact_information.email == "mfrodriguez@snecorp.com"
    assert isinstance(user_aggregate.associated_company_id, AssociatedYardOwnerCompany)
    assert user_aggregate.user.contact_information.phone_number == 50377589833
    assert user_aggregate.state.state_enum == ExampleState.CREATED

@pytest.mark.asyncio
async def test_process_event_enable_user(setup_builder):
    # Arrange
    builder = setup_builder(
        "Max Rodriguez",
        "mfrodriguez@snecorp.com",
        50377589833,
        AssociatedYardOwnerCompany("SNEA"),
        ExampleCreatedState()
    )
    
    # Act
    user_aggregate = builder.build()
    user_aggregate.approved_user("pichi")

    # Assert
    assert user_aggregate is not None
    assert user_aggregate.user.contact_information.name == "Max Rodriguez"
    assert user_aggregate.user.contact_information.email == "mfrodriguez@snecorp.com"
    assert isinstance(user_aggregate.associated_company_id, AssociatedYardOwnerCompany)
    assert user_aggregate.user.contact_information.phone_number == 50377589833
    assert user_aggregate.state.state_enum == ExampleState.CREATED

def test_build_should_throw_exception_when_user_not_specified():
    # Arrange
    builder = ExampleAggregate.builder()

    # Act & Assert
    with pytest.raises(ValueError, match="User must be specified."):
        builder.build()

def test_user_should_have_contact_information(setup_builder):
    # Arrange
    builder = setup_builder(
        "Alice Brown",
        "alicebrown@example.com",
        1122334455,
        AssociatedYardOwnerCompany("SNEA"),
        ExampleCreatedState()
    )
    
    # Act
    user_aggregate = builder.build()

    # Assert
    assert user_aggregate.user.contact_information is not None
    assert user_aggregate.user.contact_information.name == "Alice Brown"
    assert user_aggregate.user.contact_information.email == "alicebrown@example.com"
    assert user_aggregate.user.contact_information.phone_number == 1122334455

def test_user_should_have_default_status(setup_builder):
    # Arrange
    builder = setup_builder(
        "Bob White",
        "bobwhite@example.com",
        2233445566,
        AssociatedCarrierCompany("SNEA"),
        ExampleCreatedState()
    )
    
    # Act
    user_aggregate = builder.build()

    # Assert
    assert user_aggregate.state is not None
    assert user_aggregate.state.state_enum == ExampleState.CREATED
