# exit code = 0  means program executed successfully
# exit code = 1 means program has crashed


age = int(input("enter the age "))
print(age)


# Note: if you enter value eg ='dgf', the program crashes with message
# output:
# enter the age dgf
# Traceback (most recent call last):
#   File "e:\PYTHON\basic\33_exception_&_error handling.py", line 5, in <module>
#     age = int(input("enter the age "))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'dgf'


# NOTE: The program crashed just because the user entered the invalid value.So as a programer  instead of letting the program crash we have to handle the exceptions and errors and print proper error message.


# Handling error IN Python

try:
    age = int(input("enter the age "))
    print(age)
except ValueError:
    print(" value entered not valid.")

    # for input 'dgf' instead of crashing the program display message
    # " value entered not valid."

try:
    age = int(input("enter your age   :"))
    income = 100000 / age
    print(f"income = {income}")
except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print("invalid input value")
