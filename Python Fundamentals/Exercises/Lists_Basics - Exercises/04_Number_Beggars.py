# sums_list = input().split(", ")
# number_of_beggars = int(input())
# sums_list_as_diggits = [] # sums_list_as_diggits = [int(i) for i in sums_list]
#
# for diggits in range(len(sums_list)):
#     sums_list_as_diggits.append(int(sums_list[diggits]))
#
# counter_of_beggars = 0
# temp_sum = 0
# final_list = list()
# while counter_of_beggars < number_of_beggars:
#
#     for index in range(counter_of_beggars, len(sums_list_as_diggits), number_of_beggars):
#         temp_sum += sums_list_as_diggits[index]
#
#     final_list.append(temp_sum)
#     temp_sum = 0
#     counter_of_beggars += 1
#
# print(final_list)



# sums_list = input().split(", ")
# number_of_beggars = int(input())
#
# sums_list_as_int = [int(i) for i in sums_list]
#
# temp_sum = 0
# counter_of_beggars = 0
# final_list = []
#
# while counter_of_beggars < number_of_beggars:
#
#     for index in range(counter_of_beggars, len(sums_list_as_int), number_of_beggars):
#         temp_sum += sums_list_as_int[index]
#
#     final_list.append(temp_sum)
#     temp_sum = 0
#     counter_of_beggars += 1
#
# print(final_list)



# beggars = input().split(", ")
# beggars = list(map(int, beggars))  # converts the elements of a list from str to int
# count_of_beggars = int(input())
#
# wealth = []  # here you will append the re-distributed wealth of the beggars
#
# if len(beggars) < count_of_beggars:  # if the length of the list is smaller then the count, then the for cycle will give an error; the different should be represented by zeroes
#     difference = count_of_beggars - len(beggars)
#     for diff in range(difference):
#         beggars.append(0)
#
# for count in range(count_of_beggars):  # the count represents the number of times the for cycle will be repeated. The range is exclusive.
#     sum_elem = 0  # this value keeps track of the re-distributed value that will be appended. At the beginning of the new for cycle this element becomes zero.
#     index = count  # the index represents 1) the 1st index of the itteration and 2) the index of the number that needs to be added to the sum
#     while index < len(beggars):
#         sum_elem += beggars[index]
#         index += count_of_beggars  # the incrementation of this value will end the while cycle
#
#     wealth.append(sum_elem)  # the number is appended to the new list at the end of the while cycle
#
# print(wealth)



# string = list(map(int, input().split(", ")))
# beggars = [0 for i in range(int(input()))]
#
# index = 0
#
# for i in range(len(string)):
#     if index == len(beggars):
#         index = 0
#     beggars[index] += string[i]
#     index += 1
#
# print(beggars)


# nums_str = input().split(", ")
# beggars_count = int(input())
# numbers = [] # numbers = [int(i) for i in nums_str]
#
# for num in nums_str:
#     number = int(num)
#     numbers.append(number)
#
# beggars = []
#
# for i in range(beggars_count):
#     beggars.append(0)
#
# index = 0
#
# for number in numbers:
#     beggars[index] += number
#     index += 1
#
#     if index == beggars_count:
#         index = 0
#
# print(beggars)




# nums_str = input().split(", ")
# count_beggars = int(input())
#
# nums_int = [int(i) for i in nums_str]
# beggars = []
#
# for i in range(count_beggars):
#     beggars.append(0)
#
# index = 0
#
# for num in nums_int:
#     beggars[index] += num
#     index += 1
#
#     if index == count_beggars:
#         index = 0
#
# print(beggars)




numbers_str = input().split(", ")
beggars = int(input())

numbers_int = [int(i) for i in numbers_str]
beggars_count_sum = 0
count_beggars_receive = []

index = 0

for n in range(index, len(numbers_str), beggars):
    if index > len(numbers_str):
        break
    else:
        beggars_count_sum += int(numbers_str)
        numbers_str.pop(0)
        index += 1



print(count_beggars_receive)