from .animal import Animal
from .interfaces import CatInterface


class Cat(Animal, CatInterface):
    sound: str = "prrr"

    def __init__(self, name: str, energy: int):
        super().__init__(name)
        self.energy = energy

    def purr(self) -> str:
        return self.make_sound()

    def break_things(self) -> None:
        self.energy = 0

