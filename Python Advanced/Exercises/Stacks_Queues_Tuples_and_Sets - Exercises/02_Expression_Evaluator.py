from collections import deque

expression = input().split()
nums = deque()

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for ch in expression:
    if ch in "+-/*":
        while len(nums) > 1:
            left = nums.popleft()
            right = nums.popleft()
            result = operations[ch](left, right)
            nums.appendleft(result)
    else:
        nums.append(int(ch))
print(nums.popleft())





# from collections import deque
#
# string_expression = input().split()
# numbers = deque()
#
# for el in string_expression:
#     # el is operator
#     if el in "+-*/":
#         while len(numbers) > 1:
#             num_1 = numbers.popleft()
#             num_2 = numbers.popleft()
#
#             result = 0
#             if el == "+":
#                 result = num_1 + num_2
#             elif el == "-":
#                 result = num_1 - num_2
#             elif el == "*":
#                 result = num_1 * num_2
#             else:
#                 result = num_1 // num_2
#
#             numbers.appendleft(result)
#     # el is number
#     else:
#         numbers.append(int(el))
#
# print(numbers.popleft())







# from collections import deque
#
# numbers = deque()
#
# string_of_numbers = input().split()
#
# for ch in string_of_numbers:
#     if ch not in "*+-/":
#         numbers.append(int(ch))
#     else:
#         if ch == "/":
#             ch = "//"
#         result = ""
#         while numbers:
#             result += str(numbers.popleft())
#             if len(numbers) > 0:
#                 result += ch
#         result = eval(result)
#         numbers.append(str(result))
#         result = ""
#
# print(*numbers)




# sequence=[el for el in input().split()]
# numbers=[]
# for el in sequence:
#     if el.isnumeric() or el.startswith('-') and el[1:].isdigit(): # (ако ел е число)позитивно число или (ел започва със минус и ел[1:])негативно число
#         numbers.append(int(el))
#     else:
#         if el=='-':
#             number=numbers[0]
#             for el in numbers[1:]:
#                 number-=el
#             numbers.clear()
#             numbers.append(number)
#         elif el=='+':
#             number=sum(el for el in numbers)
#             numbers.clear()
#             numbers.append(number)
#         elif el=='*':
#             number = numbers[0]
#             for el in numbers[1:]:
#                 number*=el
#             numbers.clear()
#             numbers.append(number)
#         elif el=='/':
#             number = numbers[0]
#             for el in numbers[1:]:
#                 number = int(number/el)
#             numbers.clear()
#             numbers.append(number)
# print(numbers[0])



# from collections import deque
#
# string_expression = input().split()
# numbers = deque()
# operations = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a // b
# }
#
# for el in string_expression:
#     # el is operator
#     if el in "+-*/":
#         while len(numbers) > 1:
#             num_1 = numbers.popleft()
#             num_2 = numbers.popleft()
#
#             result = operations[el](num_1, num_2)
#             numbers.appendleft(result)
#     # el is number
#     else:
#         numbers.append(int(el))
#
# print(numbers.popleft())