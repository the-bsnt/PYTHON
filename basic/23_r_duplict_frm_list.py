# Program to remove the duplicates from the list

numbers = [1, 2, 4, 5, 6, 9, 3, 8, 5, 6, 7, 5, 6, 1, 7, 5, 6, 9, 8, 5, 2, 3, 7]

c = 1
for i in numbers:
    print(c, numbers)  # this is only for showing the inner process
    idx = numbers.index(i)
    c = numbers.count(i)
    for j in range(c):
        numbers.remove(i)
    numbers.insert(idx, i)
print(numbers)


# ALTERNATIVE

numbers2 = [4, 5, 8, 6, 9, 3, 2, 5, 8, 6, 4, 9, 4, 9, 5, 3, 8, 5, 2, 7, 5, 1]
noduplicate = []  # declaring empty list

for num in numbers2:
    if num not in noduplicate:  # here we use not operator and in operator
        noduplicate.append(num)
print(noduplicate)
