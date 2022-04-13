# def perfect_num(number):
#     result = 0
#     for digit in range(1, number):
#         if number % digit == 0:
#             result = result + digit
#     if result == number:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
# number = int(input())
# print(perfect_num(number))




# def perfect_num(number):
#     result = 6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128
#     perfect_numbers = list(result)
#     if number in perfect_numbers:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
# number = int(input())
# print(perfect_num(number))



def is_perfect(some_number):
    sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            sum += divisor
    if sum == some_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
print(is_perfect(number))