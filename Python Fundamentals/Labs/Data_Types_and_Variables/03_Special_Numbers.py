n = int(input())

for num in range(1, n + 1):
    nums_as_string = str(num)
    result = 0
    for symbol in nums_as_string:
        result += int(symbol)
    if result == 5 or result == 7 or result == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
#
#
# n = int(input())
#
# for num in range(1, n + 1):
#     sum_digits = 0
#     current_digit = num
#     while current_digit > 0:
#         sum_digits += current_digit % 10
#         current_digit = current_digit // 10
#     if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")


# number = int(input())
#
# for n in range(1, number + 1):
#     working_number = n
#     digit_sum = 0
#
#     while working_number > 0:
#         digit_sum += working_number % 10
#         working_number = int(working_number / 10)
#
#     is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
#     print(f"{n} -> {is_special}")