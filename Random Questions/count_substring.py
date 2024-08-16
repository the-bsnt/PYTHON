string = "BLSKDANANALSDFLK"
word = "ANA"
score = 0
idx = 0
while True:
    idx = string.find(word, idx)
    if idx == -1:
        break
    score += 1
    idx += len(word) - 1
print(score)
