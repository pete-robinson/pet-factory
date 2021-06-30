from .animal import Animal
from .interfaces import DogInterface


class Dog(Animal, DogInterface):
    sound: str = "woof"
    bones: int = 0

    def __init__(self, name: str, energy: int, bones: int):
        super().__init__(name)
        self.energy = energy
        self.bones = bones

    def bark(self) -> str:
        return self.make_sound()

    # this is a stupid method, I wasn't feeling hugely creative
    def play_fetch(self) -> None:
        print("Throwing {0} bones".format(self.bones))

        for i in range(0, self.bones):
            print("Throwing bone {0}".format(i+1))
            self.bones = self.bones - 1

            print("{0} running".format(self.name))

            print("Returned bone {0}... good doggo!".format(i + 1))
            self.bones = self.bones + 1

        print("All bones thrown")

