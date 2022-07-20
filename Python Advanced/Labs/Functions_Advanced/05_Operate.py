def operate(sign, *args):
    if sign in ("+", "-"):
        result = 0
    else:
        result = 1

    if sign == "+":
        for el in args:
            result += el
    elif sign == "-":
        for el in args:
            result -= el
    elif sign == "*":
        for el in args:
            if el == 0:
                result *= 1
            result *= el
    elif sign == "/":
        for el in args:
            if el == 0:
                result /= 1
            result /= el

    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
