names = ["john", "harry", "prabesh", "dpesh", "bsnt"]
print(
    names
)  # ---> this displays list just as it is : ['john', 'harry', 'prabesh', 'depesh']

# using index

print("1", names[2])


print("2", names[2:])  # --> this left the fist two strings in the list and print rest

print(
    "3", names[2:4]
)  # --> this prints the data from index 2 to 4(index 2 and index 3)

print("4", names[-2])  # --> this prints the second last index in list

print("5", names[-2:])  # --> this prints the  last two index in the list
print("6", names[:2])  # --> this prints the  first two index in the list

# modifying the list
names[0] = "bishal"
print(names)


# NOTE :
# Lists are a fundamental data structure in Python.
# We can modify the elements in list after they have been created.
# Lists can contain elements of different data types.
# We can add and remove elements from list.
# Lists accept duplicate data.
# Lists are part of Python's standard library, and you can create them using square brackets [ ].
