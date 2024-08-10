string = "AABCAAADA"
k = 3
t = []
u = []
for i in range(0, len(string), k):
    t.append(string[i : i + k])
for i in t:
    u.append("".join(dict.fromkeys(i)))
print("\n".join(u))
