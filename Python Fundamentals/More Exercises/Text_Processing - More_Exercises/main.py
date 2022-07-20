# Unicode_Characters

# def convert(symbol: str):
#     el = hex(ord(symbol))
#     return el[-2:]
#
#
# text = input()
# for i in text:
#     print(f'\\u00{convert(i)}', end='')
# print()




# Convert_from_Base-10_to_Base-N

# def calculate(n: int, b: int):
#     result = []
#     while not n == 0:
#         el = n % b
#         result.append(str(el))
#         n //= b
#     return ''.join(reversed(result))
#
# base, number = input().split()
# print(calculate(int(number), int(base)))




# Convert_from_Base-N_to_Base-10

# def calculate(d: str, b: int):
#     result = 0
#     x = 0
#     for el in d[::-1]:
#         result += int(el) * (b**x)
#         x += 1
#     return result
#
# base, digits = input().split()
# print(calculate(digits, int(base)))




# Magic_Exchangeable_Words

# def magic(strings: str):
#     strings = strings.split()
#     if len(strings[0]) <= len(strings[1]):
#         key_str = strings[0]
#         value_str = strings[1]
#     else:
#         key_str = strings[1]
#         value_str = strings[0]
#     compare_dict = {}
#     for el in range(len(key_str)):
#         key = key_str[el]
#         value = value_str[el]
#         if key not in compare_dict.keys():
#             if value not in compare_dict.values():
#                 compare_dict[key] = value
#             else:
#                 return False
#         else:
#             if compare_dict[key] == value:
#                 pass
#             else:
#                 return False
#     value_str = value_str[len(key_str):]
#     for el in value_str:
#         if el not in compare_dict.values():
#             return False
#     return True
#
# text = input()
# result = magic(text)
# print(str(result).lower())





# Melrah_Shake

# text = input()
# x = input()
# while True:
#     boolean = False
#     if not x:
#         break
#     tmp = text.split(x, 1)
#     if len(tmp) > 1:
#         boolean = True
#     else:
#         break
#     if boolean:
#         tmp = ''.join(tmp)
#     tmp = tmp.rsplit(x, 1)
#     if len(tmp) == 1:
#         boolean = False
#     if boolean:
#         text = ''.join(tmp)
#         print('Shaked it.')
#         x = x[:len(x) // 2] + x[len(x) // 2 + 1:]
#         if not x:
#             boolean = False
#             break
#     else:
#         break
# if not boolean:
#     print('No shake.')
#     print(text)





# Multiply_Big_Number

# x = int(input())
# print(x * int(input()))





# Sum_Big_Numbers

# def sum_big_number(number_1: str, number_2: str):
#     result = ''
#     if len(number_1) < len(number_2):
#         x = len(number_2) - len(number_1)
#         number_1 = '0' * x + number_1
#     elif len(number_2) < len(number_1):
#         x = len(number_1) - len(number_2)
#         number_2 = '0' * x + number_2
#     x = 0
#     for el in range(len(number_1) - 1, -1, -1):
#         sum_el = int(number_1[el]) + int(number_2[el]) + x
#         result += str(sum_el % 10)
#         x = sum_el // 10
#     if not x == 0:
#         result += str(x)
#     result = result[::-1]
#     # if result[0] == '0':
#     #     result = result[1:]
#     return result
#
# el1 = input()
# el2 = input()
# final_result = sum_big_number(el1, el2)
# print(final_result)





# Encrypted Message
# with key = 5
encrypted_version = [chr(ord(ch) + 5) for ch in input()]
print("".join(encrypted_version))


# Decryption Message
# with key = 5
decrypted_version = [chr(ord(ch) - 5) for ch in encrypted_version]
print("".join(decrypted_version))