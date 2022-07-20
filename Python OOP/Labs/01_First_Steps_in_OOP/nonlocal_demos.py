def f1():
    count = 10

    def f1_inner():
        def f1_innermost():
            nonlocal count  # get from parent scope
            count += 1

        f1_innermost()

    for _ in range(5):
        f1_inner()
        print(count)


def f1_2():
    count = [10]

    def f1_inner():
        def f1_innermost():
            count[0] += 1

        f1_innermost()

    for _ in range(5):
        f1_inner()
        print(count[0])


print("This is with nonlocal count --> get from parent scope")
f1()

print("-" * 10)
print("-" * 10)

print("This is with local count --> get from local scope")
f1_2()