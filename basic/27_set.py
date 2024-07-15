# NOTE 1:  Sets is the collection of unordered items.


# NOTE 2: Each element in the set must be unique and immutable( unmodifiable).


# NOTE 3: Accepatable values in set = int, float, boolen, str, tuple


# NOTE 4: Unacceptable values in set = Lists, Dictionary.       List and Dictionary cannot be stored inside sets.


set_1 = {1, 2, "str", 4, "bsnt", 17}
print(set_1)
print(type(set_1))
set_2 = {
    2,
    4,
    4,
    "str",
    2,
    "hello",
    "str",
}  # duplicate values in set are just ignored without error
print(set_2)
print(len(set_2))


# NOTE 5: To create Empty Set
empt_set = {}  # ! this is an empty dictionary. not empty set
print(type(empt_set))


empty_set = set()
print(type(empty_set))


# * SET METHODS

# 1
set_1.add("three")  # adds an element to set
print(set_1)


# 2
set_1.remove("three")  # remove an element form set
print(set_1)

# 3
set_2.clear()  # clear the set to make empty set
print(set_2)

# 4
print(set_1.pop())  # removes an random element from set and also returns that emement
print(set_1)
