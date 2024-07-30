from abc import ABC, abstractmethod


class DomainEvent:
    pass


class IDomainEventSubscriber(ABC):
    @abstractmethod
    async def notify_event_async(self, domain_event: DomainEvent):
        pass


class IDomainEventSubscriberAsync(IDomainEventSubscriber, ABC):
    @abstractmethod
    async def notify_event_async(self, domain_event: DomainEvent):
        pass


class DomainEventSubscriberBase(IDomainEventSubscriberAsync):
    @abstractmethod
    async def notify_event_async(self, domain_event: DomainEvent):
        pass

    async def notify_event_async(self, domain_event: DomainEvent):
        if isinstance(domain_event, self.__orig_bases__[0].__args__[0]):
            await self.notify_event_async(domain_event)
        else:
            raise ValueError(
                f"Invalid event type: {domain_event.__class__.__name__}, "
                f"when I'm trying to handle by {self.__class__.__name__}"
            )
