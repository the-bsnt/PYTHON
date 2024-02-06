# we can use single double and triple quotes to declare string
str1 = "this is single quoted string"
str2 = "this is double quoted string"
str3 = """this is triple quoted string"""
print(str1)
print(str2)
print(str3)
#
#
#
# to use single qoutation inside string we use double qoutation outside
print("Python's for Beginners ")
# to use double qoutation inside  string we use triple qoutation outside
print("""He like "apple " """)
#
#
#
# also to write string in paragraph form
paragraph = """
Hi Esten.X

Here is our first email to you.

Thank you,
The support Team

"""
print(paragraph)
print(str1[5])  # we can use index to get one character
print(str1[-10])  # we can also use negative index to get character ranked form end;
print(str1[0:3])  # starts from 0 index and stops at 2 [doesnt display char at index 3]
# str[start index: length]
#
#
print(str1[:])  # this prints all the characters form start to end;

str4 = str1[:]  # basically str4 is copy of str1

print(str4)
#
#
# now
print(str4[1:-1])  # this displays "his is single quoted strin"
print(str4[6:-9])
