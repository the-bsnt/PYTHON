import math

first_name = input("enter your first name ; ")
last_name = input("enter your last name : ")
space = " "
print("my full name is ", first_name, last_name)
name = first_name + space + last_name
print("the name is ", name)

# # 5
birth_year = input("what is your birth yearr.")
birth_year = input("what is your birth yearr.")
age = 2024 - int(
    birth_year
)  # birth_year is initially string datatype so needed typecasting
print("age = ", age)
# 6

age = input("Enter your age ;")
print(type(age))
print(type(int(age)))
# #7

print("This is a apple. ")
print("it's also a apple")
print("""this is triple coated string """)
print(
    """this is first paragraph
      this is second paragrapah """
)
str = "sameerbasnet"
print(str[5])
print(str[-6])
print(str[2:8])  # prints char of index 2 up to 7 not 8
print(str[:])
str2 = str
print(str2[:])
print(str2[4:-3])
print(str2[-2:8])  # not  valid
print(str2[-2:-8])  # not valid


#  #8
name = "Basnet"
prof = "programmer"
print(name, "is a professional", prof)  # strings are not concatinated.
print(name + "is a professional" + prof)  # strings are concatinated.
plus = name + "is a professional " + prof
print(plus)

message = f"Hello! My name is {name}. I am a professional {prof}"
print(message)

# 9
course = "Bachelors of Science in Computer Science and Information Technology"
# functions- len()
print(len(course))

# methods -upper, lower,
print(course.upper())
print(course.lower())
print(course.find("T"))
print(course.replace("Computer Science", "CS"))

# operator
print("echnology" in course)  # returns boolen data ie True or False
print(course)

# 10

print(100 / 5)  # returns floating data
print(100 // 5)  # returns interger number
print(103 % 5)  # for mod operation
print(5**3)  # returns 5^3  (power operator )
x = 5
x += 3
print(x)

# 12
# some math functions; round( ) abs(), methods ; ceil, floor,gcd

a = 3.4
b = 5.6
c = -44
# functions
print("Round off of a = 3.4 is ", round(a))
print("Round off of b= 5.6 is ", round(b))
print("Absolute value of c = ", abs(c))
# modules
print(math.gcd(8, 12))
print(math.floor(5.3))
print(math.ceil(5.3))

# 13 if statement
print("enter any two numbers ")
a = input()
b = input()
if a > b:
    print(a, "is greater interger than", b)
else:
    print(b, "is greater interger than", a)

# 14 logical operators

a = False
b = True
if a and b:
    print("a.b =True")
else:
    print("a.b =False")

if a or b:
    print("a+b = True")
else:
    print("a+b = False")

print("NEgation of a =", not a)
print("NEgation of b =", not b)
print("Negation of a +b = ", not (a or b))


# 16
# for loop
sum = 0
for x in [1, 2, 3, 4, 5]:
    print(x)
    sum = sum + x
print(sum)
print("_________________________\n")
for i in range(0, 10):
    print(i)
print("_________________________\n")
for i in range(2, 10, 2):  # for even numbers
    print(i)

# 17 nested loop

for i in range(1, 3):
    print("x" * 5)
    for j in range(i):
        print("x" * 2)

# 18 find largest number in the list
list = [7, 5, 6, 8, 6, 54, 2, 13, 54.5, 4, 7, 9]
list1 = list
l = list[0]
for i in list:
    if l < i:
        l = i
print(l)
# sorting in acending
for k in range(len(list) - 1):
    for i in range(len(list) - 1 - k):
        if list[i] > list[i + 1]:
            t = list[i]
            list[i] = list[i + 1]
            list[i + 1] = t
print(list)


# sorting using python library
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)


# 19 matrix

matrix = [[1, 4, 5], [7, 6, 3], [2, 8, 9]]
print(matrix)

# 20 list methods

numbers = [2, 5, 8, 7, 5, 6, 3, 4, 5, 7, 3, 0, 98, 7]
print(numbers)
numbers.insert(2, 77)
print(numbers)
numbers.pop(2)
print(numbers)
print(numbers.index(98))  # returns index
# or
print(98 in numbers)


# 21_remove duplicate numbers form the list using not in operator
list = [
    1,
    2,
    3,
    4,
    56,
    7,
    8,
    95,
    4,
    6,
    2,
    8,
    5,
    6,
    321,
    8,
    8,
    2,
    56,
    32,
    12,
    45,
    21,
    5,
    26,
    9,
    5,
    35,
    8,
]
withoutduplicate = []
for i in list:
    if i not in withoutduplicate:
        withoutduplicate.append(i)
print(withoutduplicate)


# 24_ Tuples ----[ to avoid accidently modification in list data]

Tuple_data = (1, 2, 4, 5, 6)
print(Tuple_data)
print(Tuple_data[3])
print(type(Tuple_data))
tup = ("apple",)
print(tup)

# 25_ Unpacking -- can be done with both list and tuple
tuple_ = (2, 3, "apple", "r")
a, b, c, d = tuple_
print(a)
print(b)
print(c)
print(d)

# 26 Dictionaries
pen = {"color": "red", "cost": 20, "quality": "standard"}
print(pen)
print(pen["cost"])
print(pen["quality"])


# 30 Function
# to print area of circle


def circe_area(r):
    area = (r**2) * math.pi
    return area


radius = input("enter the radius of circle -")
print(f"The area of circle is {circe_area(int(radius))}")
