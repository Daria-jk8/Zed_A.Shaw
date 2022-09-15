# Inheritance Versus Composition

# a
class Parent(object):
    def implicit(self):
        print("Parent implicit()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

print("-" * 35, "a")
dad.implicit()
son.implicit()

# b
class Parent(object):
    def override(self):
        print("Parent override()")


class Child(Parent):
    def override(self):
        print("Child override()")


dad = Parent()
son = Child()

print("-" * 35, "b")
dad.override()
son.override()

# c
class Parent(object):
    def altered(self):
        print("Parent altered()")


class Child(Parent):
    def altered(self):
        print("Child, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("Child, AFTER PARENT altered()")


dad = Parent()
son = Child()

print("-" * 35, "c")
dad.altered()
son.altered()

# d
class Parent(object):
    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")


class Child(Parent):
    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("Child, AFTER PARENT altered()")


dad = Parent()
son = Child()

print("-" * 35, "d_a")
dad.implicit()
son.implicit()
print("-" * 35, "d_b")
dad.override()
son.override()
print("-" * 35, "d_c")
dad.altered()
son.altered()

# e
class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):
    def __init__(self) -> None:
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, BEFORE PARENT altered()")
        self.other.altered()
        print("Child, AFTER PARENT altered()")


son = Child()

print("-" * 35, "e")
son.implicit()
son.override()
son.altered()
