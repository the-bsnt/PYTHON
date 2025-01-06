nam = input("Name?    ").strip()
key_text = input("Keytext? ").strip()

for i in range(len(nam)):
    encoded_text = chr(ord(nam[i]) + ord(key_text[i]) - 65)
    print(f"{nam[i]} {ord(key_text[i])-65} {encoded_text}")
