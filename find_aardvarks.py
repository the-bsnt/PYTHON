def find_aardvarks(filename):
    """
    Searches a text file for the word 'aardvark' in any letter combination.

    Args:
        filename: The name of the input file.

    Returns:
        None
    """

    with open(filename, "r") as file:
        line_number = 1
        for line in file:
            line = line.lower()
            aardvark_letters = list("aardvark")
            for char in line:
                if char in aardvark_letters:
                    aardvark_letters.remove(char)
                if not aardvark_letters:
                    print(f"Aardvark on line {line_number}")
                    break
            line_number += 1


# Example usage:
find_aardvarks("test.txt")

nam = input("Name?    ").strip()
key_text = input("Keytext? ").strip()
for i in range(len(nam)):
    encoded_text = chr(ord(nam[i]) + ord(key_text[i]) - 65)
    print(f"{nam[i]} {ord(key_text[i])-65} {encoded_text}")
