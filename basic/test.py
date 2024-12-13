def words2number(s):
    word_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
    }
    lst = s.strip().split()
    n = []
    for i in lst:
        n.append(word_dict[i])
    return int("".join(n))


print(words2number("one five two"))

# print(words2number("one five two"))
