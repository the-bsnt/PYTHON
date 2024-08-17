#
# * How They Work Together

# ^ When you use a for loop on an iterable, Python internally does the following:

# &--> Calls the __iter__() method on the iterable to obtain an iterator.
# &--> Repeatedly calls the __next__() method on the iterator until a StopIteration exception is raised.

my_list = [1, 2, 3]  # This is an iterable

# Get an iterator from the list
my_iterator = iter(my_list)

# Iterate using the iterator
while True:
    try:
        element = next(my_iterator)
        print(element)
    except StopIteration:
        break

# ^ next() method is used to access the next element of iterator sequentially.

#! If iterator is completely iterated, then it cause exception error Stop Iteration
