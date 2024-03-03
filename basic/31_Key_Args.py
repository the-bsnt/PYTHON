def function1(fname, lname):
    print(f"Hi ! My name is {fname} {lname}. And, I am professional coder.")


ln = "Basnet"
fn = "Sameer"
function1(ln, fn)
# ln and fn are positional arguments ie. position or order of arguments matters.


# 1. But In Python, We Have Keyword Arguments and for those, position does not matter.
def function1(fname, lname):
    print(f"Hi ! My name is {fname} {lname}. And, I am professional coder.")


ln = "Basnet"
fn = "Sameer"
function1(lname=ln, fname=fn)
# HERE, lname=ln is a keyword argument [parameter name followed by its value].
# With this position of arguments doesnt really matter .


# You can improve the readablity of code using  the keyword arguments .
# Example: if we have to pass the interger arguments like func(23,4,5). we can increase its readablity by using keyword arguments like func(total=23,shipping=4,discount =5).


# 2.  NOTE: Keyword Arguments should always come after positional argument.
def total(price, shipping, discount):
    total = price + shipping - discount
    print("total = ", total)


# total(shipping=45,discount=0,450)  # SyntaxError: positional argument follows keyword argument#
# This causes error because we use keyword args before positional args.
total(450, shipping=45, discount=0)  # This is right code.
