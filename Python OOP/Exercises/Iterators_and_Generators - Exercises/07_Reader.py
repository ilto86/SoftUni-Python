def read_next(*args):
    for iterable in args:
        for el in iterable:
            yield el


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)