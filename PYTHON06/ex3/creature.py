from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, creature_type: str) -> None:
        self.name: str = name
        self.creature_type: str = creature_type

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        pass


class TransformCapability(ABC):

    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
