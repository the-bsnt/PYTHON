list = []


def do_operation(operation, index=None, element=None, num=None):
    index = int()  # this line is to prevent error , if you dont still code works
    if operation == "insert":
        list.insert(index, element)
    elif operation == "print":
        print(list)
    elif operation == "remove":
        list.remove(num)
    elif operation == "append":
        list.append(num)
    elif operation == "sort":
        list.sort()
    elif operation == "pop":
        list.pop()
    elif operation == "reverse":
        list.reverse()


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        line = input()
        try:
            n = 0
            operation, index, element = line.split()
            do_operation(operation, index=int(index), element=int(element), num=int(n))
            continue
        except ValueError:
            pass
        try:
            index = element = 0
            operation, n = line.split()
        except ValueError:
            operation = line
        do_operation(operation, index=int(index), element=int(element), num=int(n))

# INPUT:
# 29
# append 1
# append 6
# append 10
# append 8
# append 9
# append 2
# append 12
# append 7
# append 3
# append 5
# insert 8 66
# insert 1 30
# insert 6 75
# insert 4 44
# insert 9 67
# insert 2 44
# insert 9 21
# insert 8 87
# insert 1 75
# insert 1 48
# print
# reverse
# print
# sort
# print
# append 2
# append 5
# remove 2
# print


# OUTPUT:
# [1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
# [5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
# [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]
