# Print the permutations of the string  on separate lines. input - > HACK 2
from itertools import permutations

word, r = input("enter input").split()
word = list(word)
word.sort()
for i in list(permutations(word, int(r))):
    i = list(i)
    print("".join(i))
