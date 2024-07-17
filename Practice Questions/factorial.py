def fact(num):
    if num == 1:
        return 1
    f = num * fact(num - 1)
    return f


print(fact(5))
