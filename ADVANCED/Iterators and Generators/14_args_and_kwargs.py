"""In Python, *args and **kwargs are special syntaxes used in function definitions to handle variable numbers of arguments. They allow functions to accept any number of positional and keyword arguments, respectively."""

# *1. *args (Positional Arguments)
"""Stands for "arguments" (or "arbitrary positional arguments").

Collects any number of positional arguments into a tuple.

Useful when you don't know how many positional arguments might be passed to the function.
"""
# Example:


def example_function(*args):
    print(args)  # args is a tuple


example_function(1, 2, 3)  # Output: (1, 2, 3)
example_function("a", "b")  # Output: ('a', 'b')
# * 2. **kwargs (Keyword Arguments)
"""Stands for "keyword arguments" (or "arbitrary keyword arguments").

Collects any number of keyword arguments (key-value pairs) into a dictionary.

Useful when you want to handle named arguments dynamically."""

# Example:


def example_function2(**kwargs):
    print(kwargs)  # kwargs is a dictionary


example_function2(name="Alice", age=25)  # Output: {'name': 'Alice', 'age': 25}
example_function2(x=1, y=2)  # Output: {'x': 1, 'y': 2}

# * Combined Usage (*args and **kwargs)
# You can use both together to handle any type and number of arguments:


def combined_example(*args, **kwargs):
    print("Positional args (tuple):", args)
    print("Keyword args (dict):", kwargs)


combined_example(1, 2, 3, name="Alice", age=25)

# ^ Output:

# Positional args (tuple): (1, 2, 3)
# Keyword args (dict): {'name': 'Alice', 'age': 25}
# In the Context of __init__ and super()


# & In your example:

"""
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

"""
# & The *args and **kwargs capture all positional and keyword arguments passed to the child class's __init__.

# & super().__init__(*args, **kwargs) passes those arguments to the parent class's __init__.

# & This is commonly used in class inheritance to ensure the parent class is properly initialized without explicitly listing all possible arguments.

# * Why Use This Pattern?
# & Flexibility: The child class doesn't need to know the exact arguments the parent class requires.

# & Maintainability: If the parent class's __init__ changes, the child class doesn't need modification.

# & Forward Compatibility: Works even if new arguments are added to the parent class.

#  Example in Inheritance:


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Parent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Passes args/kwargs to Parent.__init__


child = Child(name="Alice", age=25)  # Works!
"""
Key Takeaways:
*args → Tuple of positional arguments.

**kwargs → Dictionary of keyword arguments.

They are often used in inheritance to pass arguments to the parent class seamlessly.

The names args and kwargs are conventions; you could use *vars and **kvars, but sticking to *args/**kwargs is recommended for readability."""
