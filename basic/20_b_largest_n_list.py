# program to find the largest number in the given list

list = [7, 5, 6, 8, 6, 54, 2, 13, 54, 4, 7, 9]
# l = max(list)  # max() - function to return largest value in list
# s = min(list)  # min() - function to return smallest value in list
# print("largest number in list = ", l)
# print("smallest number in list = ", s)

# iterative method
l = list[0]
for i in list:
    if l <= i:
        l = i

print("largest number in list = ", l)

print(list)
# shorting list into ascending

for k in range(len(list) - 1):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            t = list[i]
            list[i] = list[i + 1]
            list[i + 1] = t
print(list)


# shorting using method

numbers = [4, 5, 8, 2, 9, 0, 2, 7, 8, 45, 67, 34, 79, 32, 7, 9]
print("Shorted numbers in ascending  : ")
numbers.sort()  # sort is method in python to sort list in ascending order
print(numbers)

print("Shorted numbers in descending : ")
numbers.sort(reverse=True)
print(numbers)
