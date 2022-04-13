# numbers_str = input().split()
# numbers_inverted = []
#
# for number in numbers_str:
#     number_inverted = int(number) * -1
#     numbers_inverted.append(number_inverted)
#
# print(numbers_inverted)


# n = input().split()
# reverse_nums = []
# for a in n:
#     current_num = int(a)
#     reverse_nums.append(current_num)
# nums_result = [ -x for x in reverse_nums]
# print(nums_result)



# list_of_numbers = input().split()
# oposite_numbers = [] #list()
#
# for index in range(len(list_of_numbers)):
#     oposite_numbers = -int(list_of_numbers[index])
#     oposite_numbers.append(oposite_numbers)
#
# print(oposite_numbers)


# list_of_numbers = input().split()
# oposite_numbers = [-int(s) for s in list_of_numbers]
# print(oposite_numbers)

# nums = input().split(' ')
# new_list = []
#
# for num in nums:
#     if int(num) > 0:
#         new_list.append(-int(num))
#     else:
#         new_list.append(abs(int(num)))
# print(new_list)



# nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(" ")))]
# print(nums)


numbers = input().split(" ")
numbers_int = [-int(nums) for nums in numbers]  # Invert Values  # Example -1 == 1 and 2 == -2 (list containing the opposite of each number)

print(numbers_int)