#
# *  In Python, try, except, and raise are used for exception handling. They help you manage errors gracefully and maintain the flow of your program.

# * try and except
# & These are used to catch and handle exceptions (errors) that might occur in your code.

# ^ Syntax:

try:
    # Code that might raise an exception
    print("try")
except SomeError:
    # Code to handle the exception
    print("except: someerror")

# & Example:

try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
# Output:

# Cannot divide by zero!


# * raise
# & The raise statement is used to manually trigger an exception. It can be helpful when you want to stop the program if a certain condition is met or propagate an error for the caller to handle.

# ^ Syntax:

# ^ raise Exception("Custom error message")

# & Example:


def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age is {age}")


try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")
# Output:

# Error: Age cannot be negative!


# * Combining try, except, else, and finally
# *You can extend exception handling using else and finally:

# & else: Executes if no exception is raised.
# & finally: Always executes, whether an exception occurs or not (often used for cleanup).
# Example:

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")


# * Summary:
# ^ try: Code that might raise an exception.
# ^ except: Handle specific exceptions.
# ^ raise: Manually raise an exception.
# ^ else: Executes if no exception occurs.
# ^ finally: Always runs, used for cleanup.
