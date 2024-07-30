from dependency_injector.wiring import inject
from faimly_t_ddd_core.common.faimly_t_python_framework_data_access_cosmos.cosmos_sql.event_repository.event_repository import EventRepository

class ExampleEventsRepository(EventRepository):
    def __init__(self, 
                 config, 
                 logger):
        super().__init__(config, logger)
