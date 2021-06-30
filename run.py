from classes.animal_factory import (AnimalFactory, AnimalTypes)
from classes.interfaces import (CatInterface, DogInterface)

# init the factory
factory = AnimalFactory()

# test 1 - create a dog
print("Test 1 - create a dog")

dog_data = {
    "name": "Smithy",
    "energy": 200,
    "bones": 3,
    "type": AnimalTypes.DOG
}

# build the dog animal
doggo = factory.build_animal(dog_data)

# get_name is ubiquitous to all subclasses due to it living in the parent
print("Dog created. It's name is {0}".format(doggo.get_name()))

# bark() and play_fetch() are unique to Dog
print(doggo.bark())
doggo.play_fetch()


print("\n\n")


# test 2 - create a cat
print("Test 2 - create a cat")

cat_data = {
    "name": "Sheba",
    "energy": 100,
    "type": AnimalTypes.CAT
}

catto = factory.build_animal(cat_data)
print("Cat created. It's name is {0}".format(catto.get_name()))

# again, methods unique to the Cat class
print(catto.purr())
# break things... as cats to
catto.break_things()
print(catto.energy)


print("\n\n")


# test 3 - create a test table of different animal types and run sequenced code for each
print("Test 3 - create a bunch of animals")

animals = [
    {"name": "Dog 1", "energy": 100, "bones": 3, "type": AnimalTypes.DOG},
    {"name": "Dog 2", "energy": 50, "bones": 4, "type": AnimalTypes.DOG},
    {"name": "Cat 1", "energy": 10, "type": AnimalTypes.CAT},
    {"name": "Dog 3", "energy": 150, "bones": 5, "type": AnimalTypes.DOG},
    {"name": "Cat 2", "energy": 100, "type": AnimalTypes.CAT},
]

for x in animals:
    a = factory.build_animal(x)

    if isinstance(a, CatInterface):
        animal_type = "Cat"
    elif isinstance(a, DogInterface):
        animal_type = "Dog"

    print("Animal created. It's a {0} and it's name is {1}".format(animal_type.lower(), a.get_name()))




