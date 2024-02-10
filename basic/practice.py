# first_name = input("enter your first name ; ")
# last_name = input("enter your last name : ")
# space = " "
# print("my full name is ", first_name, last_name)
# name = first_name + space + last_name
# print("the name is ", name)

# # 5
# birth_year = input("what is your birth yearr.")
# birth_year = input("what is your birth yearr.")
# age = 2024 - int(birth_year) # birth_year is initially string datatype so needed typecasting
# print("age = ", age)
# #6

# age = input("Enter your age ;")
# print(type(age))
# print(type(int(age)))
# #7

# print("This is a apple. ")
# print("it's also a apple")
# print("""this is triple coated string """)
# print(
#     """this is first paragraph
#       this is second paragrapah """
# )
# str = "sameerbasnet"
# print(str[5])
# print(str[-6])
# print(str[2:8])  # prints char of index 2 up to 7 not 8
# print(str[:])
# str2 = str
# print(str2[:])
# print(str2[4:-3])
# print(str2[-2:8])
# print(str2[-2:-8])


#  #8
# name = "Basnet"
# prof = "programmer"
# print(name, "is a professional", prof)  # strings are not concatinated.
# print(name + "is a professional" + prof)  # strings are concatinated.
# plus = name + "is a professional " + prof
# print(plus)

# message = f"Hello! My name is {name}. I am a professional {prof}"
# print(message)

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
