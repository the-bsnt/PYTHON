course = "Bachelors of Science in Computer Science and Information Technology "
print(len(course))  # gives the length of string;

print(course.upper())
print(course)

# upper is a method [ function] that converts all string char. to uppercase
#
# this method upper doesnot change the original string but takes string, change it , and return it ;
#
# print() and len() are  general purpose functions
#
# but upper() is a method that works for only strings;

print(course.lower())  # prints all char. in lower case
#
#
#
print(course.find("o"))
# find index in which character is located. It is [case sensitive]
print(
    course.replace("Information Technology", "IT")
)  # it replaces "Information Technology " with "IT" ..##[ case sensitive]
#
#
#
print(
    "Science" in course
)  # in is an operator that returns boolean value whether "Science" is in course string
print("science" in course)  # returns as "False" because [ case sensitive  ]
