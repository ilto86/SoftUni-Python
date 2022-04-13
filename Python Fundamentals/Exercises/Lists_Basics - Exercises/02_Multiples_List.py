# factor = int(input())
# count = int(input())
# current_factor = factor
# my_list = []
# my_list.append(factor)
#
# for _ in range(count -1):
#     current_factor += factor
#     my_list.append(current_factor)
#
# print(my_list)


# factor = int(input())
# count = int(input())
# list_of_numbers = [] #list()
#
# for multiplier in range(1, count + 1):
#     list_of_numbers.append(factor * multiplier)
#
# print(list_of_numbers)


# num1 = int(input())
# num2 = int(input())
# new_list = []
#
# for num in range(1, num2 + 1):
#     new_list.append(num * num1)
# print(new_list)



numbers = int(input())
count = int(input())
result = 0
new_list = []

for nums in range(1, count +1):
    result = nums * numbers
    new_list.append(result)
print(new_list)