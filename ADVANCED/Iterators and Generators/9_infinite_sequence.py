def infinite_sequence():
    term = 1
    while True:
        yield term
        term *= 3  # geometric sequence with common ratio 3


value = infinite_sequence()
for i in range(10):
    print(next(value))
