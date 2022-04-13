# def character_long(str_num):
#     is_valid = True
#     if not 5 < len(str_num) < 11:
#         is_valid = False
#         print("Password must be between 6 and 10 characters")
#
#     for char in str_num:
#         if char.isdigit() or char.isalpha():
#             continue
#         else:
#             is_valid = False
#             print("Password must consist only of letters and digits")
#             break
#     digits = 0
#     for char in str_num:
#         if char.isdigit():
#             digits += 1
#
#     if digits < 2:
#         is_valid = False
#         print("Password must have at least 2 digits")
#
#     return is_valid
#
# password = list(input())
# is_valid = character_long(password)
#
# if is_valid:
#     print("Password is valid")





password = input()
nums = 0
condition = True

if not 6 <= len(password) <= 10:
    condition = False
    print("Password must be between 6 and 10 characters")

for char in password:
    if char.isdigit() or char.isalpha():
        continue
    else:
        condition = False
        print("Password must consist only of letters and digits")
        break

for char in password:
    if char.isdigit():
        nums += 1

if nums < 2:
    condition = False
    print("Password must have at least 2 digits")

if condition:
    print ("Password is valid")