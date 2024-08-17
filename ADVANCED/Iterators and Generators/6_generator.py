def generator(n):
    for i in range(n):
        yield i**2


generator_obj = generator(6)

print(next(generator_obj))
print(next(generator_obj))
print(next(generator_obj))
print(next(generator_obj))
print(next(generator_obj))
