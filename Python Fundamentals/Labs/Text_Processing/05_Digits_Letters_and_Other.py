# text = input()
# digits = ""
# letters = ""
# symbols = ""
#
# for char in text:
#     if char.isdigit():
#         digits += char
#     elif char.isupper() or char.islower():  # elif char.isalpha():
#         letters += char
#     else:
#         symbols += char
# print(digits)
# print(letters)
# print(symbols)




# text = input()
# digits = ""
# letters = ""
# symbols = ""
#
# for char in text:
#     if char.isalnum():
#         if char.isdigit():
#             digits += char
#         else:
#             letters += char
#     else:
#         symbols += char
# print(digits)
# print(letters)
# print(symbols)



word = input()

digits = ""
letters = ""
others = ""

for char in word:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(digits)
print(letters)
print(others)