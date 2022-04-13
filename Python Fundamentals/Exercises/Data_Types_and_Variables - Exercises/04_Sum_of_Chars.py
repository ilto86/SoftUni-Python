# n = int(input())
# total_sum = 0
#
# for let in range(n):
#     letter = input()
#     total_sum += ord(letter)
# print(f"The sum equals: {total_sum}")



number = int(input())
total_sum = 0

for _ in range(number):
    char = input()
    total_sum += ord(char)
print(f"The sum equals: {total_sum}")