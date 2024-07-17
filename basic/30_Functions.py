def function1():
    print(f"This is a function1.")
    for i in range(6):
        print(">", i)


# NOTE- PEP8: Expected 2 blank lines after class or function defination. [best practice for formating our code]
print("calling a function...")
function1()
print("function end")


def intro(firstname, lastname):
    print(f"Hi {firstname} {lastname}!")
    print("How are you? Welcome to ITTI.")


fn = "Basnet"
ln = "Sameer"
intro(fn, ln)


lst = ["sameer", 17, "basnet"]


def print_list(list):
    for i in lst:
        print(i, end=" ")


print_list(lst)
print(flush=True)  # flushes the input buffer(istream) like space or anything else


# * RETURN Statement


def square(n):
    s = n**2
    print(f"square = {s}")


print(square(8))
# Output :
# square = 64
# None

# NOTE: By default, python interpetor return value none in case of absence of return statement
