# Some Conventions used in Python

# * PascalCase for Class Names in Python


class Car:
    pass


class ElectricCar:
    pass


# * Functions
# ^ snake_case: Use lowercase letters with underscores to separate words.


def calculate_area(length, width):
    pass


# * Variables
# ^ snake_case: Similar to function names.

total_count = 0
product_price = 9.99


# * Constants
# ^ ALL_CAPS: Use uppercase letters with underscores for constants.

MAX_VALUE = 100
PI = 3.14159


# * Modules and Packages
# ^ snake_case: For module and package names.

import Python_Package.my_module
from Python_Package import my_module


# * Exceptions
# ^ PascalCase: Similar to class names.
class MyCustomError(Exception):
    pass


class FileNotFoundError(Exception):
    pass


# * Protected and Private Members

# ^ Single underscore: For protected members (accessible within the class and its subclasses).


class MyClass1:
    def __init__(self):
        self._protected_attribute = "value"


# ^ Double underscore: For private members (intended for internal use only).


class MyClass2:
    def __init__(self):
        self.__private_attribute = "value"


# * Other Considerations

# & Descriptive names: Use clear and meaningful names that reflect the purpose of variables, functions, and classes.

# & Avoid single-letter names: Unless used for very short-lived variables in small scopes.

# & Consistency: Adhere to consistent naming conventions throughout your codebase.

# & PEP 8 is the official style guide for Python code. It provides comprehensive recommendations for naming conventions, formatting, and other coding practices.
