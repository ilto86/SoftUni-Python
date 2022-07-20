# Global namespace - pi and sum1 (global for this module)
from math import pi


def f1():
    pi = 3.14
    print(pi)


def sum1(ll):
    # result and x - in local namespace (local for func body and class)
    result = 5
    for x in ll:
        result += x
    return result


# print and sum - built-in namespace
print(sum([1, 2, 3, 4]))                # sum - built-in namespace

print(sum1([1, 2, 3, 4]))               # sum1 - Global namespace - pi and sum1 (global for this module)

print(pi)                               # pi - built-in namespace

f1()                                    # f1_pi - Global namespace - pi (global for this module)

print(pi)                               # pi - built-in namespace