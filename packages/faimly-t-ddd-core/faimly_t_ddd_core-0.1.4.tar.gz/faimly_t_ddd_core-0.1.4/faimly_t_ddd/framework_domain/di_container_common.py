
from dependency_injector import containers, providers

from faimly_t_ddd.framework_domain.domain_events.domain_event_publisher import DomainEventPublisher
from faimly_t_ddd.framework_domain.validation_commands.validation_behavior import IPipelineBehavior, ValidationBehavior


class DIContainerCommon(containers.DeclarativeContainer):
    domain_event_publisher = providers.Factory(DomainEventPublisher)
    validation_behavior = providers.Factory(IPipelineBehavior, ValidationBehavior)
    
    def add_common_services(self):
        self.domain_event_publisher()
        self.validation_behavior()
