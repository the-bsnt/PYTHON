def infinite():
    i = 1
    while True:
        yield i**2
        i += 1


value = infinite()
print(value)
print(next(value))
print(next(value))
print(next(value))

# for i in value:  # iterator
#     print(i)
