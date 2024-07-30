import pytest
from unittest.mock import AsyncMock
from uuid import UUID

from faimly_t_ddd_core.infrastructure.data_access.repository.example_repository import ExampleRepository
from faimly_t_ddd_core.core.domain.example_agg.example_aggregate import ExampleAggregate
from faimly_t_ddd_core.core.domain.example_agg.specifications.example_by_id_specification import ExampleByIdSpecification
from faimly_t_ddd_core.core.domain.example_agg.specifications.example_by_scac_owner_specification import ExampleGetByScacOwnerSpecification
from faimly_t_ddd_core.core.domain.example_agg.value_objects.example_associated_company import AssociatedYardOwnerCompany
from faimly_t_ddd_core.core.domain.example_agg.value_objects.states.example_created_state import ExampleCreatedState

from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.configurations_helper import ConfigurationsHelper
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.cosmos_collection_repository import CosmosCollectionRepository
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.event_repository.event_repository import EventRepository

class TestUserIntegration():
    @pytest.fixture(autouse=True)
    def setup(self):        
        cosmos_event_config = ConfigurationsHelper("EventsExampleDb").get_cosmos_configuration("ConnectionStrings__CosmosAccountConnStr", "EventsExampleDb")
        event_repository = EventRepository(cosmos_event_config)
        self.example_repository = ExampleRepository(event_repository)

    @pytest.mark.asyncio
    async def test_create_new_agreement(self):
        # Arrange
        user = ExampleAggregate.builder() \
            .with_user(
                "Max Rodriguez",
                "mfrodriguez@snecorp.com",
                50377589833) \
            .with_associated_entity(
                AssociatedYardOwnerCompany("SNEA")) \
            .with_state(ExampleCreatedState()) \
            .build()

        # Act
        user.approved_user("pichi")
        await self.example_repository.save_async(user)

        # Assert
        assert user is not None

    @pytest.mark.asyncio
    async def test_get_yard_location(self):
        # Arrange
        p_guid = "0c87f4f9-e228-42e8-b5a9-aba59b6413a6"
        p_id = UUID(p_guid)
        get_user_by_id = ExampleByIdSpecification(p_id)

        # Act
        user_aggregate = await self.example_repository.get_by_specification_async(get_user_by_id)

        # Assert
        assert user_aggregate is not None
        assert len(user_aggregate.aggregate_event_stream.aggregate_events) > 0

    @pytest.mark.asyncio
    async def test_get_all_users_by_scac(self):
        # Arrange
        get_carrier_by_scac = ExampleGetByScacOwnerSpecification("SNEA")

        # Act
        carrier_found = await self.example_repository.get_by_specification_async(get_carrier_by_scac)

        # Assert
        assert carrier_found is not None
        assert len(carrier_found) > 0
