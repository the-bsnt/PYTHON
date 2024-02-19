# # While loops

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# For Loops
for a in ["sameer ", "basnet", "string"]:
    print(a)

for i in range(1, 10):  # form 0 to 9
    print(i)
print("_________________________\n odd numbers:")
# to print odd numbers

for i in range(1, 10, 2):
    print(i)
print("_________________________")
list = [20, 30, 50, 60, 45]
total = 0
for i in list:
    total += i
print("total = ", total)
