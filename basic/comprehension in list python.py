x = int(input("enter x "))
y = int(input("enter y "))
z = int(input("enter z "))
n = int(input("enter n "))
matrix = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            lst = [i, j, k]
            matrix.append(lst)
result = [x for x in matrix if x[0] + x[1] + x[2] != n]
print(result)
