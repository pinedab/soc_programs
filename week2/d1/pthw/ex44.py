# Exercise 44 - Inheritance vs Composition
# Parent and child interactions (3 ways)
# 1. Actions on the child imply an action on the parent.


class ParentA(object):

    def implicit(self):
        print("PARENTA implicit()")


class ChildA(ParentA):
    pass


dad = ParentA()
son = ChildA()

dad.implicit()
son.implicit()

# 2. Actions on the child override the action on the parent.


class ParentB():
    def override(self):
        print("PARENTB override()")


class ChildB(ParentB):
    def override(self):
        print("CHILDB override()")


mom = ParentB()
daughter = ChildB()

mom.override()
daughter.override()

# 3. Actions on the child alter the action on the parent,
# but then get the og version.


class ParentC(object):

    def altered(self):
        print("PARENTC altered()")


class ChildC(ParentC):

    def altered(self):
        print("CHILDC, BEFORE PARENTC altered()")
        super(ChildC, self).altered()
        print("CHILDC, AFTER PARENTC altered()")


auntie = ParentC()
baby = ChildC()

auntie.altered()
baby.altered()


# !!!!!!!!!!!!!!!!
# I could have placed all functions into one class -____-
# super() used to access parent features