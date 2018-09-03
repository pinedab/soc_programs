# Exercise 42 - IS-A, HAS-A, OBJECTS, AND CLASSES

## Animal is-a object (yes, dort of confusing) look at the EC
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        # Cat has-a name
        self.name = name

## Person is-a Object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog('Rover')

## satan is-a cat
satan = Cat("Satan")

## Maria is-a Person
maria = Person("Maria")

## Maria has-a dog
maria.pet = rover

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a cat
frank.pet = satan

## flipper is a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
