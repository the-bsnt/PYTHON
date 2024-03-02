# In Python, Unpacking is the process of extracting values from a sequence
# [Tuples or List] and assigning them to multiple variables.

# Unpacking Tuples

coordinate = (2, 5, 4)

# Usually, for assigning values of tuple to variable; we do

# x = coordinate[0]
# y = coordinate[1]
# z = coordinate[2]

# In python, we have special feature of Unpacking , that is;

x, y, z = coordinate  # Unpacking Tuples
print(x)
print(y)
print(z)

# Similarly, Unpacking List

list1 = [2, 5, 6, 3]
a, b, c, d = list1
print(a, b, c, d)


# NOTE While Unpacking, we must assign tuple data with enough variables. We
# cannot left some tuple data unassigned.

tuple2 = (1, 2, 3, 5, 6)
# l, m, n = tuple2    #ValueError: too many values to unpack (expected 3)

# Similarly with List
list3 = [7, 8, 6, 9, 5, 6]
# p, q, r = list3  # ValueError: too many values to unpack (expected 3)
