# Emoji Convertion using dictionary.
msg = input(">")
words = msg.split(" ")
# print(words)
emojis = {":)": "😊", ":(": "😒", ":{": "😖"}
output = ""
for str in words:
    output += emojis.get(str, str) + " "
print(output)
