# 1. Tuples are like lists. NOTE A Tuple is ordered and unmodifiable.

Tuple_data = (1, 2, 4, 5, 6)
print(Tuple_data)
print(Tuple_data[3])

# But we can't modify or assign the Tuple index with new Data.

# Tuple_data[3] = 76  --TypeError: 'tuple' object does not support
#                                   item assignment


# Tuples are useful if you want you list of data not be accidently
# modified in the program

# 2. From Python's perspective,
#    tuples are defined as objects with the data type 'tuple'
print(type(Tuple_data))

# 3. Allow Duplicates and different data types
Tuple_data2 = (
    "apple",
    2,
    "ball",
    "apple",
    2,
)
print(Tuple_data2)

# 4. NOTE One item tuple, remember the comma AFTER the item:
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = "apple"  # thistuple = ("apple")
print(type(thistuple))

