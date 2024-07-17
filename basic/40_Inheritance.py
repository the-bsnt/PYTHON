class Parent:
    def __init__(self, a):
        self.a = a
        print("parent class")
        print("a = ", self.a)

    def walk(self):
        print("the cat walks")


class Child(Parent):
    def __init__(self, a):
        Parent.__init__(self, a)


C1 = Child(45)
