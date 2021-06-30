# Just a quick demo for a friend

Nothing groundbreaking here, just referencing object factories for a friend.

## ./run.py
A simple demo of the class structure. Run it and compare the output with the code to see how it's working.

## classes/animal_factory.py
This is your factory. It defines an enum with your different instance types.

Given a dict of data with a `type` key, it'll compare that to the enum to work out which type of object to create

## classes/animal.py
This is your abstract parent. It contains all the functionality that is common to all implementations of it.

## classes/cat.py
The Cat variant of your base class (Animal)

## classes/dog.py
The Dat variant of your base class (Animal)

## classes/interfaces.py
Not necessary for this example but may be as your use-case gets more involved.
Basically using them as a way of type-checking the result when creating data based on iterating a sequence of data so your code knows which type of implementation you're dealing with. 