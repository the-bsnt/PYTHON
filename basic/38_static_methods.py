# STATIC METHODS


# ^      --methods that dont use self parameter.
# ^      --Self Parameter is a reference to the Current Instance of the class ie.object SO, if there is no need of object in method then there is no point to use self parameter. So we use decorator [ @static method ] and avoid use of self parmeter
# ^      --static method are methods at class level.


class Test:
    def __init__(self):
        print("constructor invoked")

    @staticmethod  # ^ decorator
    def static_method():
        print("this is static method ", end=" ")
        print("it doesnot take self argument")


T1 = Test()
T1.static_method()


# ^ NOTE: Static method is created only one time in the memory. The method is not created for every new instance, is created only for one time


# * Decorator
# *      --a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function, without permanently modifying it.
