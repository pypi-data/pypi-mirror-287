from faimly_t_ddd.framework_data_access.cosmos_sql.event_repository.event_repository import EventRepository


class ExampleEventsRepository(EventRepository):
    def __init__(self, 
                 config, 
                 logger):
        super().__init__(config, logger)
