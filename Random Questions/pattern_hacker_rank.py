n = int(input("Enter the term"))
for i in range(1, 2 * n, 2):
    txt = "H" * i
    print(txt.center(2 * n - 1, " "))

for i in range(n + 1):
    print(" " * (n // 2), end="")
    txt = "H" * n
    print(txt, end="")
    ftxt = txt.rjust(4 * n, " ")
    print(ftxt)

for i in range((n // 2) + 1):
    print(" " * (n // 2), end="")
    print("H" * n * 5)

for i in range(n + 1):
    print(" " * (n // 2), end="")
    txt = "H" * n
    print(txt, end="")
    ftxt = txt.rjust(4 * n, " ")
    print(ftxt)
for i in range(2 * n, 1, -2):
    print(" " * 4 * n, end="")
    txt = "H" * (i - 1)
    print(txt.center(2 * n - 1, " "))
