# itertools.permutations(permutable_list,r])
from itertools import permutations

print(permutations(["a", "b", "c"]))
# OUTPUT:
# <itertools.permutations object at 0x000001E0D74B3330>

print(list(permutations(["a", "b", "c"])))
# OUTPUT:
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

print(list(permutations(["a", "b", "c"], 2)))
# OUTPUT:
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

print(list(permutations("abc", 3)))
# OUTPUT:
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
