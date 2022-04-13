# def smallest_number(some_numbers):
#     return min(some_numbers)
#
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
# numbers = [number_1, number_2, number_3]
# print(smallest_number(numbers))


# def small_number(a, b, c):
#     print(min(small_number(a, b, c)))
#
# num_1, num_2, num_3 = int(input()), int(input()), int(input())
# small_number(num_1, num_2, num_3)


def small_number(a, b, c):
   return min((a, b, c))

num_1, num_2, num_3 = int(input()), int(input()), int(input())
print(small_number(num_1, num_2, num_3))
