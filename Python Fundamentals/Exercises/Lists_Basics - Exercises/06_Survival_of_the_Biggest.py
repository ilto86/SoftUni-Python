# numbers_str = input().split()
# n = int(input())
#
# for i in range(len(numbers_str)):  # numbers_list_as_int = [int(i) for i in numbers_str]
#     numbers_str[i] = int(numbers_str[i])
#
# for i in range(n):
#     min_element = min(numbers_str)
#
#     numbers_str.remove(min_element)
#
# for i in range(len(numbers_str)):  # numbers_list_as_str = [str(i) for i in numbers_list_as_int]
#     numbers_str[i] = str(numbers_str[i])
# print(", ".join(numbers_str))



# numbers_str = input().split()
# n = int(input())
# numbers_int = [int(i) for i in numbers_str]
#
# for i in range(n):
#     min_element = min(numbers_int)
#     numbers_int.remove(min_element)
#
# numbers_str = [str(i) for i in numbers_int]
# print(", ".join(numbers_str))



# numbers = list(map(int, input().split()))
# count = int(input())
#
# sorted_nums = [i for i in sorted(numbers, reverse=True)[:len(numbers) - count]]
# print(", ".join([str(i) for i in numbers if i in sorted_nums]))

# numbers_str = input().split()
# count = int(input())
# numbers_int = [int(elements) for elements in numbers_str]
#
# for i in range(count):
#     numbers_int.remove(min(numbers_int))
#
# numbers_str = [str(index) for index in numbers_int]
# print(", ".join(numbers_str))



nums = input().split(" ")
copy_nums = list(map(int, nums)) # [int(elements) for elements in nums]
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(", ".join(nums))