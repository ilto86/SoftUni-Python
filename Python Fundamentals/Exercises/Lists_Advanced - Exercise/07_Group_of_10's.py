# import math
# numbers = [int(x) for x in input().split(", ")]
# groups = (max(numbers)) / 10
# for group in range(1, math.ceil(groups) + 1):
#     print(
#         f"Group of {group}0's: {[numbers[x] for x in range(len(numbers)) if numbers[x] in range(group * 10 - 10 + 1, group * 10 + 1)]}")



# numbers = input().split(", ")
# numbers = list(map(lambda x: int(x), numbers))
# group_number = 10
# old_number = 0
# while len(numbers) > 0:
#     group = [x for x in numbers if x in range(old_number,group_number+1)]
#     print(f"Group of {group_number}'s: {group}")
#     old_number = group_number
#     numbers = list(filter(lambda x: x not in group,numbers))
#     group_number += 10




# number_list = list(map(int, input().split(", ")))
#
# group = 10
#
# while True:
#     if len(number_list) == 0:
#         break
#
#     current_list = [x for x in number_list if x <= group]
#
#     for y in current_list:
#         number_list.remove(y)
#
#     print(f"Group of {group}'s: {current_list}")
#     group += 10




sequence_of_numbers = list(map(int, input().split(", ")))

boundary = 10

while len(sequence_of_numbers) > 0:

    result = [num for num in sequence_of_numbers if num <= boundary]
    sequence_of_numbers = [num for num in sequence_of_numbers if num not in result]
    print(f"Group of {boundary}'s: {result}")
    boundary += 10