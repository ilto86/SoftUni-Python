# result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(' ')))))
# print(result)


# def check_even(number):
#     if number % 2 == 0:
#         return True
#
#     return False
#
# result = filter(check_even, list(map(int, input().split(' '))))
# print(list(result))


# numbers = input().split()
# numbers_as_digits = []           # [int(x) for x in numbers]
# for number in numbers:           # [int(x) for x in numbers]
#     numbers_as_digits.append(int(number))   # [int(x) for x in numbers]
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, numbers_as_digits))
# print(result)


# def check_even(number):
#     if number % 2 == 0:
#         return True
#
#     return False
#
# result = filter(check_even, list(map(int, input().split(' '))))
# print(list(result))



def is_even(number):
    if number % 2 == 0:
        return True
    return False

numbers = input().split()
filtered_numbers = []
for number in numbers:
    if is_even(int(number)):  # if is_even(int(number)) == True
        filtered_numbers.append(int(number))
print(filtered_numbers)