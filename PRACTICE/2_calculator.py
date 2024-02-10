# program for simple calculation
a = int(input("Enter first interger "))
b = int(input("Enter second interger"))
print("a for add\n s for subtract\n m for multiplication \n d for divide  ")
op = input("what to do ?")
if op == "a":
    result = a + b
elif op == "s":
    result = a - b
elif op == "m":
    result = a * b
elif op == "d":
    result = a / b
else:
    print("error")
print("The result is", result)

# or
print(f"Result is {result}")
