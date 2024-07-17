#  When a function call itself repeatedly.
def print_num(n):
    if n == 0:  # *basic case
        return
    print(n)
    print_num(n - 1)


print_num(10)
print("...end")


# Factorial of a number


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print("...end")


# to print list
def printlist(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    printlist(list, idx + 1)
    return


lst = [4, 5, 6, 86, 9, 5, 6, 4, 5, 5]
printlist(lst)
print("...end")
