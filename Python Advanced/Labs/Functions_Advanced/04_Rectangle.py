def rectangle(x, y):
    def area():
        return x * y

    def perimeter():
        return 2 * (x + y)

    if not isinstance(x, int) or not isinstance(y, int):
        return 'Enter valid values!'

    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print(rectangle(2, 10))