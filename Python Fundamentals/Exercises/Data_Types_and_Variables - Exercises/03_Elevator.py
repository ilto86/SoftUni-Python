# import math
#
# n = int(input())
# p = int(input())
#
# result = n / p
# print(math.ceil(result))

n_persons = int(input())
p_capacity_of_persons = int(input())

courses = n_persons // p_capacity_of_persons

if n_persons % p_capacity_of_persons > 0:
    courses += 1

print(courses)
