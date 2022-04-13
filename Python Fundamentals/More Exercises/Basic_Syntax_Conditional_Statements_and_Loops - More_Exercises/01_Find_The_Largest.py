# num = input()
#
# dig_list = [dig for dig in str(num) if dig.isnumeric()]
# dig_list.sort(reverse=True)
#
# print(''.join(dig_list))



# s = input()
# digits = sorted(s, reverse=True)
# print(int(''.join(digits)))



# number = input()
#
# list_numbers = []
# for i in number:
#     i = int(i)
#     list_numbers.append(i)
# list_numbers.sort(reverse=True)
# print(*list_numbers, sep='')



# num = input()
#
# num = list(num)
# num.sort(reverse=True)
#
# string = ''
#
# for i in num:
#     string += i
# print(string)



# number = int(input())
# count = [0 for x in range(10)]
# string = str(number)
# for i in range(len(string)):
#     count[int(string[i])] = count[int(string[i])] + 1
# result = 0
# multiplier = 1
# for i in range(10):
#     while count[i] > 0:
#         result = result + (i * multiplier)
#         count[i] = count[i] - 1
#         multiplier = multiplier * 10
#
# print(result)



num = input()

num = list(num)
max_num = ""
min_num = ""
string = ""
max_num_seconds = ""
min_num_seconds = ""

for i in num:
    max_num = max(list(num))
    min_num = min(list(num))
    if i > min_num and i < max_num:
        max_num_seconds = i
    for i in range(len(num)):
        if i == 1:
            string = max_num_seconds
        if i == 2 or i == 3:
            min_num_seconds = max_num_seconds
        if max_num_seconds > min_num_seconds:
            string = min_num_seconds

print(max_num, end="")
print(max_num_seconds, end="")
print(string, end="")
print(min_num)