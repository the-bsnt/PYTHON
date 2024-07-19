class Student:  # * This is class
    name = "basnet"


s1 = Student()  # * this is object
print(s1.name)


# ^ Methods
class Method_:
    def __init__(self):
        print("this is default construcor")

    def methd(self, name, age):  # & this is method
        self.name = name
        self.age = age
        print("this is method")
        print(f"the name is {name}. And Age = {age}")


M = Method_()
M.methd("hari", 25)

# * Delete Keyword
print(M.age)
del M.age
# print(M.age)  #!AttributeError: 'Method_' object has no attribute 'age'

# also
print(M.name)
del M
# print(M.name) #!NameError: name 'M' is not defined
