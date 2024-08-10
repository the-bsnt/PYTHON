# Enter your code here. Read input from STDIN. Print output to STDOUT
# X = no of items
# sizes = list of items
# N = no of demanded items
# 6 55 = size price
# calculate total price from available items
from collections import Counter

X = int(input())
sizes = list(map(int, input().split()))
sizes = Counter(sizes)
N = int(input())
demand = []
total = 0
for i in range(N):
    # demand.append(list(map(int,input().split())))
    s, price = map(int, input().split())
    count = sizes.get(s, 0)
    if count > 0:
        sizes[s] = count - 1
        total += price
print(total)

# INput
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
