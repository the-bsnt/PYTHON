class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class toyota(car):
    def __init__(self, name, type):
        super().__init__(type)  # ^ super() refers the parent class or superclass
        self.name = name
        super().start()
        car.stop()


car1 = toyota("land cruiser", "suv")
print(car1.name)
print(car1.type)


# ^ The super() builtin returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.


# ^ NOTE:Adaptability: If you have to change the inheritance structure later, you don't need to modify the code using super(); it will automatically adjust.
