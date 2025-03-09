# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
A = []
B = []
idx_dict = defaultdict(list)
for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())
for idx, value in enumerate(A):
    idx_dict[value].append(idx + 1)
for val_b in B:
    # * print(*idx_dict.get(val_b,[-1]))   # here * is unpacking operator and works as same as below
    print(" ".join(map(str, idx_dict.get(val_b, [-1]))))


"""    
Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output

1 2 4
3 5

"""
