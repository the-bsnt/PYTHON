def print_rangoli(size):
    asc = 97 + size - 1
    if size == 1:
        print(chr(asc))
        return
    alpha_list = []
    for i in range(asc, 96, -1):
        c = chr(i)
        alpha_list.append(c)
        print("-".join(alpha_list).rjust(2 * size - 1, "-"), end="-")
        rev = alpha_list[::-1]
        rev.pop(0)
        print("-".join(rev).ljust(2 * size - 3, "-"))
    for i in range(size - 1, 0, -1):
        alpha_list.pop(i)
        print("-".join(alpha_list).rjust(2 * size - 1, "-"), end="-")
        rev.pop(0)
        print("-".join(rev).ljust(2 * size - 3, "-"))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
