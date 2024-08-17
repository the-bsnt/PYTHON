#
# * How Iterators and Iterables Are Stored in Memory


# * Iterable:

# ^  An iterable is any Python object that implements the __iter__() method and returns an iterator. When you create an iterable (like a list), Python allocates memory to store the entire collection of items (e.g., integers in a list). The iterable's memory structure includes a reference to the sequence of elements.

# * Iterator:

# ^ An iterator object is usually more lightweight in memory compared to the iterable. It typically contains:

#! A reference to the iterable or sequence.
#! An internal state, such as an index or pointer, to keep track of the current position in the sequence.

# ^ The memory structure of an iterator doesn't store the entire sequence of items. Instead, it refers back to the iterable (or another data structure) and maintains just enough information to know where it is in the iteration process.
