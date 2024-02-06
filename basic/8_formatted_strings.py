# formated strings
name = "Basnet"
prof = "coder"
# now to print string "Basnet is a coder "
# This can be done with string concatination like:
print(name + " is a professional " + prof)
# but it is not ideal as our text gets more complicated;
# we use f"string"
# this helps to print the string in formatted way
message = f"{name} is a {prof} "
print(message)
msg = f"Hello, This is {name}. And I am a {prof}."
print(msg)
