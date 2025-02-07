#
# * List comprehension in Python is used to create new list by iterating over an existing iterable. (list, set, queryset, etc)

# & Syntax: [expression for item in iterable if condition]

# * -expression: The value to include in the new list.
# *-item: The current element from the iterable.
# * -iterable: Any iterable (like a list, range, or string).
# * -if condition (optional): Filters elements based on a condition.


# & normal code
num_list = [2, 3, 4, 6, 7, 5, 9, 1]
even_list = []
for i in num_list:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)

# & using list comprehension

even = [i for i in num_list if i % 2 == 0]
print(even)


# & for square list

squares = [x**2 for x in num_list]
print(squares)  # Output: [4, 9, 16, 36, 49, 25, 81, 1]
