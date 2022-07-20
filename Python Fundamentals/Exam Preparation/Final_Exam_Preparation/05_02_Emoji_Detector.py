# import re
#
# text = input()
#
# cool_threshold = 1
#
# for number in text:
#     if number.isdigit():
#         cool_threshold *= int(number)
#
# print(f'Cool threshold: {cool_threshold}')
#
# pattern = r'::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*'
# matches = re.findall(pattern, text)
#
# print(f'{len(matches)} emojis found in the text. The cool ones are:')
#
# cool_emojis = []
# for index in matches:
#     coolness = 0
#
#     for char in index[2 : -2]:
#         coolness += ord(char)
#
#     if coolness > cool_threshold:
#         cool_emojis.append(index)
#
# for cool_emoji in cool_emojis:
#     print(cool_emoji)


# import re
#
# text = input()
# pattern = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
# cool_emojis = []
# cool_threshold = 1
#
# emojis = re.findall(pattern, text) # returns all matches in a List
#
# for i in text:
#     if i.isdigit():
#         cool_threshold *= int(i)
#
# for emoji in emojis:
#     sign = 0
#     for ch in emoji[2:-2]:
#         sign += ord(ch)
#     if sign > cool_threshold:
#         cool_emojis.append(emoji)
#
# print(f'Cool threshold: {cool_threshold}')
# print(f'{len(emojis)} emojis found in the text. The cool ones are:')
#
# [print(x) for x in cool_emojis]





# import re
#
# text = input()
# cool_threshold = 1
#
# numbers = "\d"
# result = re.findall(numbers, text)
#
# for nums in result:
#     cool_threshold *= int(nums)
# print(f"Cool threshold: {cool_threshold}")
#
# pattern = "::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
# matches = re.findall(pattern, text)
#
# emojis = []
# found_emojis = []
# for match in matches:
#     found_emojis.append(match)
#     emoji_coolnes = 0
#     for char in match:
#         if char.isalpha():
#             emoji_coolnes += ord(char)
#     if emoji_coolnes >= cool_threshold:
#         emojis.append(match)
#
# print(f"{len(found_emojis)} emojis found in the text. The cool ones are: ")
# for emoji in emojis:      # [print(emoji) for emoji in emojis]
#     print("".join(emoji))


# import re
#
# text = input()
# regex = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'
#
# cool_threshold = 1
#
# for d in text:
#     if d in '0123456789':
#         cool_threshold *= int(d)
#
# print(f"Cool threshold: {cool_threshold}")
#
# emojis = []
# matches = re.finditer(regex, text)
#
# for emoji in matches:
#     emojis.append(emoji.group(0))
#
# print(f"{len(emojis)} emojis found in the text. The cool ones are:")
#
# for emoji in emojis:
#     coolness_sum = 0
#     for d in emoji[2:-2]:
#         coolness_sum += ord(d)
#
#     if coolness_sum > cool_threshold:
#         print(emoji)




import re

text = input()
pattern = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
matches = re.findall(pattern, text)
num_matches = re.findall(r"\d", text)
cool_threshold = 1

for num in num_matches:
    cool_threshold *= int(num)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    cool_emoji = 0
    for char in match:
        if char.isalpha():
            cool_emoji += ord(char)
    if cool_emoji >= cool_threshold:
        print(match)