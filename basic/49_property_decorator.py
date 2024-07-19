# here is an example
class marks:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        self.percentage = (self.phy + self.che + self.math) / 3


m1 = marks(98, 76, 38)
print(f"{m1.percentage}%")
m1.che = 45  #! if you change the marks of any subject later the percentage is not gonna change
print(m1.che)
print(f"{m1.percentage}%")


# TODO in this type of situation where one attribute depends on another or we cannot give the attribute a fixed value , we can we seperate method and call it


class Student:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        self.percentage = (self.phy + self.che + self.math) / 3

    def calc_percentage(self):
        self.percentage = (self.phy + self.che + self.math) / 3


S1 = Student(78, 56, 38)
print(f"{S1.percentage}%")

S1.che = 88
S1.calc_percentage()
print(f"{S1.percentage}%")


# * BUT we can use property decorator for better code to do the same task.


class StudentI:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math

    @property
    def percentage(self):
        return round((self.phy + self.che + self.math) / 3)


S1 = StudentI(98, 97, 95)
print(f"{S1.percentage}%")

S1.che = 88
print(f"{S1.percentage}%")
# ^ Here, property decorator allows us to use percentage method [function] as property (ie.S1.percentage) so that if other attributes changes then percentage also updates automatically.
