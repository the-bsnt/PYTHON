class Test:
    def __init__(self):
        pass

    def talk(self):
        print("to demonstrate the example of ")


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        try:
            print(f"Hi, I am {self.name}. And I am {self.age} years old")
        except:
            print("one of the attribute; either name or age is missing ")


P1 = Person("Hari", 21)
P1.talk()
P1.age = 15
P1.talk()
P2 = Person("Prabesh", 22)
P2.talk()
del P2.age
P2.talk()
del P2
# P2.age = 4  gives error
