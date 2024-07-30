from abc import ABC, abstractmethod


class BaseState(ABC):
    def __init__(self, state_enum):
        self.state_enum = state_enum

    @abstractmethod
    def handle(self, aggregate):
        pass

    def __str__(self):
        return self.state_enum.name.replace("State", "")
