from enum import Enum
from .cat import Cat
from .dog import Dog

# using an enumerator to add governance to data types
class AnimalTypes(Enum):
    CAT = 1
    DOG = 2


# factory class to build animal types
class AnimalFactory:

    # public method - build me an animal
    def build_animal(self, data):
        # compare data.type against enum values
        if data["type"] == AnimalTypes.CAT:
            return self.__build_cat(data)
        elif data["type"] == AnimalTypes.DOG:
            return self.__build_dog(data)

    # private method because the outside world shouldn't have visibility of these methods
    # separate method to build a cat
    def __build_cat(self, data) -> Cat:
        obj = Cat(data["name"], data["energy"])
        return obj

    # separate method to build a dog
    def __build_dog(self, data) -> Dog:
        obj = Dog(data["name"], data["energy"], data["bones"])
        return obj

