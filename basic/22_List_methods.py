# List MEthods ->These are the operations we perfrom on the list.

numbers = [2, 4, 6, 3, 8, 9]

# 1     .append(data)       --to add a new item to the list from last
numbers.append(7)
print(numbers)

# 2     .insert(index,data) --to insert a new item to specific index to the list.
numbers.insert(1, 5)
print(numbers)

# 3     .pop(index)         --to delete the specific index and data in that index
numbers.pop(2)
print(numbers)

# 4     .remove(data)       --to remove specific data from the list
numbers.remove(8)
print(numbers)

# 5     .clear()            --to clear the list
numbers.clear()
print(numbers)

dataA = [7, 3, 4, 3, 5, 6, 1, 3, 8, 3]

# 6     .index(data)            --returns the index in which the give data lie
print("index = ", dataA.index(1))
# whatif the number is not in list.
# print(list.index(77))  # --ValueError 77 is not in list

# alternative
print(77 in dataA)  # --returns boolean value. [safer to use]

# 7     .count(data)            --to count the reoccurance of data item
print(dataA.count(3))

# 8     .copy()                 --returns the copied list.
dataB = dataA.copy()
print(dataA)
# 9     .sort()                 --to sort the give list in ascending
dataA.sort()
print(dataA)
#       to sort descending order
dataA.sort(reverse=True)
print(dataA)

# NOTE
print("data = ", dataB)  # --change in dataA brings no change in data B
