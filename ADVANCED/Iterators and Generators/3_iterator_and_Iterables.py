lst = [3, 56, 45, 9, 6, 5, 6, 3, 15, 9, 6, 3, 54, 8, 5, 2, 3, 6, 41]
# ^ lst [List] is a an Iterable.
# ^ object that can be iterated over the loop

# for i in lst:
#     print(i)

print(lst)

# *  To convert iterable to iterator

lst_iterator = iter(lst)
# ^ lst_iterator is an Iterator.
# ^object which provides the way to access elements in list sequentially. ie. iterate upon the loop.


# for i in lst_iterator:
#     print(i)
print(lst_iterator)  # ^ <list_iterator object at 0x000001ACD4B85B70>

print(next(lst_iterator))  # prints first elements in the list
print(next(lst_iterator))  # prints second elements in the list
print(next(lst_iterator))  # prints third elements in the list
print(next(lst_iterator))  # prints fourth elements in the list

# ie. you can access the list sequentially one by one
