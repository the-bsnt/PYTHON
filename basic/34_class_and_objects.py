class Test:
    def __init__(self):
        print("first class")


# All classes have a function called __init__(), which is always executed when the class is being initiated.
# NOTE: The __init__() function is called automatically every time the class is being used to create a new object.


# object
obj = Test()


class Point:
    x = int()
    y = int()

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.y = 20
point1.draw()
point1.move()
point1.x = 5
print(point1.x)

point2 = Point()
print(point2.x)
