#   Program that takes number and return into word
num = input("enter your phone number  ")  # takes input as string
ntow = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
output = ""
for ch in num:
    output += ntow.get(ch, "!") + " "
    # a space " " is added at end so that words are not close to each other.
print(output)
