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
