# Default Constructor
class Test:
    def __init__(self):
        print("this is default constructor")


T = Test()


# Paramaterized Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("this is paramaterized constructor")


P1 = Person("basnet", 20)


# Single constructor with optional Arguments
class Book:
    def __init__(self, b_name=None, page_nos=None):
        self.b_name = b_name
        self.page_nos = page_nos
        print(f"This is constructor with optional arguments")
        print(f"Book Name = {b_name}")
        print(f"Page Numbers= {page_nos}")


B = Book()
B = Book("DSA", 455)
