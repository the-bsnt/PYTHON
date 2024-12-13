pairs = []  # List to store name and colour pairs

while True:
    entry = input("Name and colour: ").strip()
    if entry == "":  # Stop if the input is empty
        break
    pairs.append(entry)

# Print the stored pairs
for pair in pairs:
    print(pair)
