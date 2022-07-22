def fibonacci():
    first = 0
    second = 1

    yield first
    yield second

    while True:
        result = first + second
        first, second = second, result
        yield result


generator = fibonacci()
for i in range(5):
    print(next(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))

# print(("=" * 20))
#
# generator = fibonacci()
# for i in range(10):
#     print(next(generator))