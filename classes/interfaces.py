from abc import ABC, abstractmethod


class DogInterface(ABC):
    @abstractmethod
    def bark(self) -> str:
        pass

    @abstractmethod
    def play_fetch(self) -> None:
        pass


class CatInterface(ABC):
    @abstractmethod
    def purr(self) -> str:
        pass

    @abstractmethod
    def break_things(self) -> None:
        pass

