name = input("enter your name:      ")
weight = len(name)
print(weight)
if weight < 3:
    print("error: name must be at least 3 characters long.")
elif weight > 50:
    print("error: name can be maximum of 50 characters long.")
else:
    print("name look good!")
