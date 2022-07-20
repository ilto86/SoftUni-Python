# file = open('./numbers.txt', 'r')
# the_sum = 0
#
# for line in file:
#     the_sum += int(line)
#
# print(the_sum)
import current as current

# with open("numbers.txt") as file:
#     result = 0
#     for line in file.readlines():
#         current_num = int(line)
#         result += current_num
# print(result)

# try:
#     with open("numbers.txt") as file:
#         print(sum([int(line_num) for line_num in file.readlines()]))
#         # result = 0
#         # for line in file.readlines():
#         #     current_num = int(line)
#         #     result += current_num
#         # print(result)
# except FileNotFoundError:
#     print("File not found")




try:
    with open("numbers_in_one_line.txt") as file:
        print(sum([int(line_num) for line_num in file.read().split()]))
except FileNotFoundError:
    print("File not found")