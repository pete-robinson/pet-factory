from abc import (ABC, abstractmethod)

# This class is essentially abstract...
# The methods within this class are common to all implementations of it


class Animal(ABC):
    energy: int = 0
    sound: str = ""
    name: str = ""

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def eat(self, food: int) -> int:
        self.energy += food
        return self.energy

    def make_sound(self) -> str:
        return self.sound + "!!!"

