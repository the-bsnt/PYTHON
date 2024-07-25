# Enter your code here. Read input from STDIN. Print output to STDOUT
n, three_n = map(int, input().split())
pt = ".|."
for i in range(1, n, 2):
    ptt = pt * i
    print(ptt.center(three_n, "-"))
print("WELCOME".center(three_n, "-"))
for i in range(n - 2, 0, -2):
    ptt = pt * i
    print(ptt.center(three_n, "-"))
