#
# * Class and Instance Attributes in Python

# ^ Python Class Attributes    --> variables of a class that are shared between all of its instances

# ^ Python Instance Attributes -->  variables of a class are owned by one specific instance of the class and are not shared between instances.

#! NOTE: Class Attributes in Python are takes as Static data members as in C++ or Java. And Instance Attributes in Python are taken as normal Data members as in C++.


class ExampleClass:
    class_attr = 17

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr
        return


E = ExampleClass(5)
print(E.class_attr)
print(E.instance_attr)


# ? instance_attr --> an instance attribute defined inside the constructor.
# ? class_attr --> a class attribute defined outside the constructor.

# * Properites of Class Attribute
# 1. Defined outside the constructor
# 2. get Stored only one time in the memory, when first object is created.
# 3. is acessible as both a property of the class and as a property of objects, as it’s shared between all of them.[#^can be accessed by Class Name]
print(ExampleClass.class_attr)  # ExampleClass is a Class Name here.


# * Properties of Instance Attributes
# 1. defined inside the constructor.
# 2. declared and initialized every time when new object is created.
# 3. cannot be acessed by Class Name, shows #& [Attribute Error]

# ! NOTE:The class attribute can be accessed as a class property and as an instance property, however, accessing an instance attribute as a class property raises an AttributeError.
