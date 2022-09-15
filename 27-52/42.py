# Is-A, Has-A, Objects, and Classes

# 1st
class Animal(object):
    pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name


# 2nd
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None


class Empoyee(Person):
    def __init__(self, name, salary):
        super(Empoyee, self).__init__(name)
        self.salary = salary


# 3rd
class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")
mary.pet = satan

frank = Empoyee("Frank", 120000)
frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
