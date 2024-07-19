# Conceptual Implemtation in Python
# * Private (like) Attributes and Methods

# * Private Attributes and Methods are meant to be accessed only within class and not to be acessed outside the class.

# NOTE: They are just like private data members in C++.


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # ^Private Attribute

    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account(123456789, "aldkfjsld")

print(acc1.acc_no)
#! print(acc1.__acc_pass)       AttributeError: 'Account' object has no attribute '__acc_pass'
# ^ This is because __acc_pass is private attribute and cannot be accessed outside the class.


# & But private attributes or methods can be accessed by the methods inside class.
# example

acc1.reset_pass()


# Example
class Person:
    def __init__(self) -> None:
        pass

    def __get(self, name, age):
        self.name = name
        self.age = age
        print(f"My name is {name} and i am {age} years old.")

    def access_get(self, name, age):
        self.__get(name, age)


P = Person()
#! P.__get("basnet", 21)       AttributeError: 'Person' object has no attribute '__get'
#! You cannot access __get() method directly by object as it is private attribute. But __get() Method can be accessed using another public method ie. access_get()

P.access_get("basnet", 21)
