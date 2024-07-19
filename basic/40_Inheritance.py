#       INHERITANCE
# * Single Level Inheritance
class Parent1:
    def __init__(self, a):
        self.a = a
        print("parent class")
        print("a = ", self.a)

    def walk(self):
        print("the cat walks")


class Child1(Parent1):
    def __init__(self, a):
        Parent1.__init__(self, a)


C1 = Child1(45)
C1.walk()


# * Multi Level Inheritance
class Grand_Parent:
    def __init__(self):
        print("grandparent")


class Parent2(Grand_Parent):
    def __init__(self):
        Grand_Parent.__init__(self)
        print("parent")


class Child2(Parent2):
    def __init__(self):
        Parent2.__init__(self)
        print("child")


# ^GrandParent ---> Parent ---> Child

C2 = Child2()


# *   Multiple Inheritance
class Parent_I:
    def __init__(self):
        print("parent first")


class Parent_II:
    def __init__(self):
        print("parent second")


class Child_(Parent_II, Parent_I):
    def __init__(self):
        Parent_I.__init__(self)
        Parent_II.__init__(self)
        print("child")


cc = Child_()
# ^ Parent_I + Parent_II ---> Child
