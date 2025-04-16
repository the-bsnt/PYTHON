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


# * Thinking

# & 🔤 Etymology: Why "constructor"?
""" The name constructor comes from its purpose — it constructs (builds) the object.

When you create an object from a class, the constructor is the special function that:

--Sets up the internal structure of the object.
--Initializes member variables.
--Ensures the object starts life in a valid state.

So, it's literally constructing the object into usable form.

It's like saying:

“Hey, I've got this class blueprint. Let's construct a real thing out of it!”
"""

# & 🔧 What exactly does a constructor do in C++?
"""In C++, a constructor:

--Has the same name as the class.

--No return type, not even void.

--Is automatically called when the object is created.

--Can be overloaded (multiple versions with different parameters).

--Can be default, parameterized, copy, or move constructor.

When you write:


Student s("David", 21);
→ You're constructing the object s, using that constructor to fill in the name and age.
"""

# & 🧱 Why not call it "initializer"?
"""Good question. Some languages do have initializers (e.g., Swift has init()), but in C++:

Constructors do both: they create and initialize.

The name emphasizes that this is more than just assigning values — it's about building the actual object.

In technical terms, construction comes before initialization in C++ object lifecycle, especially in complex classes with inheritance and memory allocation.

"""
