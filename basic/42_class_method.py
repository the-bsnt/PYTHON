# Trying to change the class attribute.
class Person:
    name = "anonymous"

    def changename(self, name):
        self.name = name


P1 = Person()
P1.changename("hari aryal")
print(P1.name)  # ?          prints hari aryal
print(Person.name)  # ?      prints anonymous

#! this signifies that we cannot change the class attribute simply just by calling normal method.
# & in above, when we call changename() method and try to change name attribute , Here new instance name attribute is created by [self.name] and initialized with the give parameter. it has nothing to do with class attribute. class attribute is still the same.


# TODO To change the class attribute


# * Class Method
class Person_II:
    name = "anonymous"

    # def changename(self, name):
    #     self.name = name
    @classmethod  # ^ decorator
    def changename(cls, name):
        cls.name = name


P2 = Person_II()
P22 = Person_II()
P2.changename("basnet sameer")
print(P2.name)  # ?             prints basnet sameer
print(Person_II.name)  # ?      prints basnet sameer
print(P22.name)  # ?            prints basnet sameer
# all three prints basnet sameer
# & the class attribute name is change by this way and is same for all objects .


# TODO:     Alternative Methods
class Student:
    name = "anonymous"
    rollno = 25

    def changename(self, name, rollno):
        Student.name = name  # ^            technique1 --> to access the class attribute
        self.__class__.rollno = rollno  # ^ technique2 --> to access the class attribute


S1 = Student()
S2 = Student()
S1.changename("manzil gautam", 108)

print(S1.name)
print(Student.name)
print(S2.name)
# all three prints manzil gautam
# & the class attribute name is change by this way and is same for all objects .
