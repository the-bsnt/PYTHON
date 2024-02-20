for i in range(4):  # loop from 0 to 3
    for j in range(3):
        print(f"({i},{j})")
print(f"finished with ({i},{j})")
print("----------------------------------")

# Display the pattern
# xxxxx
# xx
# xxxxx
# xx
# xx

for i in range(1, 3):
    print("x" * 5)
    for j in range(i):
        print("x" * 2)
print("----------------------------------")
# or without using inner loop .
x = [5, 2, 5, 2, 2]
for i in x:
    print("x" * i)
print("----------------------------------")
