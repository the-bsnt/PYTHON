# To represent matrix using 2D lists
_2Dlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(_2Dlist)
x = int(input("enter x "))
y = int(input("enter y "))
z = int(input("enter z "))
# n = int(input())
matrix = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            lst = [i, j, k]
            matrix.append(lst)
print(matrix)
