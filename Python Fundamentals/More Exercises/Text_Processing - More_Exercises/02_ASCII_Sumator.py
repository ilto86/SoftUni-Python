# def find_ascii_sum(char1, char2, chars):
#     START = ord(char1)
#     END = ord(char2)
#     ascii_values = []
#     for char in chars:
#         if START < ord(char) < END:
#             ascii_values.append(ord(char))
#
#     return sum(ascii_values)
#
# char_one = input()
# char_two = input()
# characters = input()
# print(find_ascii_sum(char_one, char_two, characters))




# first_char = input()
# second_char = input()
# random_string = input()
#
# start = min(ord(first_char), ord(second_char)) + 1
# end = max(ord(first_char), ord(second_char))
# char_range = range(start, end)
#
# total = 0
#
# for char in random_string:
#     if ord(char) in char_range:
#         total += ord(char)
#
# print(total)




# first_char = ord(input())
# second_char = ord(input())
# text = input()
#
# total_sum = 0
#
# for char in text:
#     if first_char < ord(char) < second_char:
#         total_sum += ord(char)
#
# print(total_sum)





first_symbol = ord(input())
second_symbol = ord(input())
text = input()

result = 0

for char in text:
    if first_symbol < ord(char) < second_symbol:
        result += ord(char)

print(result)



# valid_range = range(ord(input())+1, ord(input()))
# print(sum([ord(char) for char in input() if ord(char) in valid_range]))