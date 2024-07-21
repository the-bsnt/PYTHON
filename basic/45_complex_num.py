class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(f"{self.real} + {self.img}i")

    #! def add(self, num2):
    #!     r = self.real + num2.real
    #!     i = self.img + num2.img
    #!     return Complex(r, i)
    def __add__(self, num2):  # * Using dunder function (double underscore funcion)
        r = self.real + num2.real
        i = self.img + num2.img
        return Complex(r, i)

    def __sub__(self, num2):  # * Using __sub__() dunder function
        r = self.real - num2.real
        i = self.img - num2.img
        return Complex(r, i)


num1 = Complex(4, 5)
num1.show()
num2 = Complex(5, 2)
#! num3 = num1.add(num2))
num3 = num1 + num2
num3.show()
