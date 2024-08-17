import sys


def generator(n):
    for i in range(n):
        yield i**3


terms = generator(100)
values = generator(10000000)

print(sys.getsizeof(terms))
print(sys.getsizeof(values))

# * NOTE: Here, Despite how we change the value of n , the size of the generator_obj is not gonna change.[ As generator_obj is iterator and can be iterated upon to get values]

# ^The entire sequence is not gonna store in the memory. The values are generated only when needed.
