# def recursive_power(number, power):
#     if power == 0:  # if power == 1:
#         return 1    # return number
#     return number * recursive_power(number, power - 1)
#
#
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))


def recursive_power(x, y):
    if y == 0:     # if y == 1
        return 1   # return x
    return x * recursive_power(x, y - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))