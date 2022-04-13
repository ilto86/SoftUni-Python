# divisor = int(input())
# bound = int(input())
# max_multiplier = 0
# for current_number in range(divisor + 1, bound + 1):
#     if current_number % divisor == 0:
#         max_multiplier = current_number
# print(max_multiplier)


# divisor = int(input())
# bound = int(input())
# max_multiplier = 0
# for current_number in range(bound, divisor,- 1):
#     if current_number % divisor == 0:
#         max_multiplier = current_number
#         break
# print(max_multiplier)


# first_number = int(input())
# second_number = int(input())
#
# result = int(second_number / first_number) * first_number
# print(result)


# first_number = int(input())
# second_number = int(input())
#
# result = second_number -(second_number % first_number)
# print(result)


first_number = int(input())
second_number = int(input())

result = second_number // first_number * first_number
print(result)