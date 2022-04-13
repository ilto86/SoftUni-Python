# start_char = int(input())
# end_char = int(input())
#
# for letter in range(start_char, end_char + 1):
#     if letter == end_char:
#         print(chr(letter), end="")
#     else:
#         print(chr(letter), end=" ")



start_interval = int(input())
final_interval = int(input())

for num in range(start_interval, final_interval + 1):
    print(chr(num), end=" ")