from collections import deque


def list_manipulator(numbers, command, position, *args):
    numbers_list = numbers
    args_numbers = list(args)

    if command == "remove":
        if position == "end":
            if args_numbers:
                [numbers_list.pop() for _ in range(*args_numbers)]
                return numbers_list
            else:
                numbers_list.pop()
                return numbers_list
        else:
            numbers_list = deque(numbers_list)
            if args_numbers:
                [numbers_list.popleft() for _ in range(*args_numbers)]
                return list(numbers_list)
            else:
                numbers_list.popleft()
                return list(numbers_list)

    elif command == "add":
        if position == "end":
            numbers_list.extend(args_numbers)
            return numbers_list
        else:
            args_numbers.extend(numbers_list)
            return args_numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))



# def list_manipulator(numbers, command, position, *args):
#     list_numbers = numbers
#     args_numbers = args
#     new_list = []
#
#     if command == "remove":
#         if position == "end":
#             if args_numbers:
#                 for _ in range(*args_numbers):
#                     list_numbers.pop()
#                     new_list = list_numbers
#             else:
#                 list_numbers.pop()
#                 new_list = list_numbers
#
#         elif position == "beginning":
#             if args_numbers:
#                 for _ in range(*args_numbers):
#                     list_numbers.pop(0)
#                     new_list = list_numbers
#             else:
#                 list_numbers.pop(0)
#                 new_list = list_numbers
#
#     elif command == "add":
#         if position == "end":
#             for number in args_numbers:
#                 list_numbers.append(number)
#                 new_list = list_numbers
#         else:
#             for number in args_numbers:
#                 new_list.append(number)
#             for number in list_numbers:
#                 new_list.append(number)
#
#     return new_list

#
# from collections import deque
#
#
# def list_manipulator(nums: list, add_remove: str, beginning_end: str, *args) -> list:
#     retval = deque(nums)
#
#     if add_remove == 'add':
#         if beginning_end == 'beginning':
#             retval.extendleft(reversed([arg for arg in args]))
#         elif beginning_end == 'end':
#             retval.extend([arg for arg in args])
#
#     elif add_remove == 'remove':
#         if beginning_end == 'beginning':
#             if args:
#                 for _ in range(args[0]):
#                     if retval:
#                         retval.popleft()
#             else:
#                 if retval:
#                     retval.popleft()
#
#         elif beginning_end == 'end':
#             if args:
#                 for _ in range(args[0]):
#                     if retval:
#                         retval.pop()
#             else:
#                 if retval:
#                     retval.pop()
#
#     return [el for el in retval]
#
#
# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
# print(list_manipulator([1, 2, 3], "remove", "end", 2))
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))