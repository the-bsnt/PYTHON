# INIT Function or Constructor in Python
class Test:
    def __init__(self):
        print("first class")


# * All classes have a function called __init__(), which is always executed when the class is being initiated.
# NOTE: The __init__() function is called automatically every time the class is being used to create a new object. In other words __init__() is constructor in python

# object
obj = Test()


# * NOTE: Constructor always take parameter which is Self Parameter.
# * The Self Parameter is a reference to the Current Instance of the class ie.object, and is used to access variables that belongs to the class.
class Note:
    a = 9
    b = 4

    def prt(self):
        print(self.a + self.b)
        print(self)


N = Note()
N.prt()
print(N)


# * self parameter ---> points the object at instance.ie
# *                ---> used to access variables that belong to that class.
# *                ---> contains the address of the that object.
# *                ---> is first parameter.
class BOOK:
    def __init__(self, bookname):
        self.name = bookname
        print("adding new book to library")


B1 = BOOK("DSA")
print(B1.name)


#:NOTE:self parameter can be named as any name.
class Other:

    def __init__(bsnt, name, a):
        bsnt.name = name
        print(bsnt.name)


O = Other("basnet", 17)
