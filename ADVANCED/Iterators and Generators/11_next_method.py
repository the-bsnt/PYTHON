#
# ? When you call next(iterator) in Python, a series of steps occur under the hood to retrieve the next item from the iterator. Here's what happens:

# * Step-by-Step Process


# ^-->Invoke the __next__() Method:

# & The next() function is essentially a wrapper that calls the iterator's __next__() method.
# Python translates next(iterator) into iterator.__next__().


# ^-->Access the Current Item:

# !The __next__() method accesses the current item in the sequence. This could be by indexing (for a list), moving a pointer (for a linked list or push/pop in stack), or through some other means, depending on the underlying data structure.

# ^-->Advance the Internal State:

# & After returning the current item, the iterator increments its internal index by 1.
# For example, if the iterator is iterating over a list, it increments its internal index by 1. This way, the next time __next__() is called, it returns the next item in the sequence.

# ^-->Return the Current Item:

# The __next__() method returns the current item to the caller.

# ^-->Handle End of Iteration:

# &If the iterator has no more items to return (i.e., it has reached the end of the sequence), the __next__() method raises a StopIteration exception.
# This exception signals to the caller that the iteration is complete.


# * First next(iterator) Call:

# & 1). iterator.__next__() is called.
# & 2). The iterator's internal state points to the first item in iterable or sequence of items.
# & 3). It returns the current value and updates its internal state to point to the second item.
