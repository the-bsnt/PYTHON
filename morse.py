def morse_varient(text):
    result = []
    text = text.lower()

    for char in text:
        if char.isalpha():
            position = ord(char) - ord("a") + 1
            result.append(f"{char}{position}beep")
        elif char == " ":
            result.append("stop")
    return "".join(result)


input_text = "hi there"
print(morse_varient(input_text))
