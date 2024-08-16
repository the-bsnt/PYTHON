import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius


C1 = Circle(7)
print(round(C1.area(), 2))
print(round(C1.perimeter(), 2))
