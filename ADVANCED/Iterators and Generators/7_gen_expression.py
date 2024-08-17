generator_experession = (i**2 for i in range(5))

# ^ generator_expression is already a generator object,so no need to call generator function. You can directly use generator_expression as Generator object

# generator_obj = generator_experession()  |instead use expression name as generator object
# generator_obj = generator_experession
print(next(generator_experession))
print(next(generator_experession))
print(next(generator_experession))
print(next(generator_experession))
print(next(generator_experession))
