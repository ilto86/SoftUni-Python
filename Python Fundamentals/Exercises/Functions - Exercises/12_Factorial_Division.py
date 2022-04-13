# import math
#
# print("The factorial of 5 is : ", end="")
# print(math.factorial(5))
#
# print("The factorial of 2 is : ", end="")
# print(math.factorial(2))
#
# print("The factorial of 5 and 2 is : ", end="")
# print(math.factorial(5) / math.factorial(2))
#
# print("The factorial of 6 is : ", end="")
# print(math.factorial(6))
#
# print("The factorial of 2 is : ", end="")
# print(math.factorial(2))
#
# print("The factorial of 6 and 2 is : ", end="")
# print(math.factorial(6) / math.factorial(2))




# from math import factorial
#
#
# def factorialDiv(num1, num2):
#     div = factorial(num1) / factorial(num2)
#     print(f'{div:.2f}')
#
#
# num1, num2 = int(input()), int(input())
# factorialDiv(num1, num2)





# def factorial(num):
#     return 1 if num == 0 or num == 1 else num * factorial(num - 1)
#
#
# number1 = int(input())
# number2 = int(input())
# result = factorial(number1) / factorial(number2)
# print(f"{result:.2f}")



# def factorial(num):
#     f = 1
#     if num >= 1:
#         for i in range(1, num + 1):
#             f = f * i
#     return f
#
#
# number1 = int(input())
# number2 = int(input())
# result = factorial(number1) / factorial(number2)
# print(f"{result:.2f}")


# def calculation(first_number, second_number):
#     for factorial in range(1, first_number):
#         first_number *= factorial
#     for factorial in range(1, second_number):
#         second_number *= factorial
#     result = first_number / second_number
#     return f"{result:.2f}"
#
#
# number1 = int(input())
# number2 = int(input())
# print(calculation(number1, number2))



# def factorial(number):
#     for factorial in range(1, number):
#         number *= factorial
#     return number
#
# first_number = int(input())
# second_number = int(input())
# first_result = factorial(first_number)
# second_result = factorial(second_number)
# result = first_result / second_result
# print(f"{result:.2f}")

import math
print(f"{math.factorial(int(input())) / math.factorial(int(input())):.2f}")