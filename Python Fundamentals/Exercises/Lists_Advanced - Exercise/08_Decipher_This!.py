# secret_message = input().split()
# decipher = list()
# numbers = []
# str1, str2, str3, str4, str5, str6 = "", "", "", "", "", ""
# counter, counter2 = 0, 0
#
# for el in secret_message:
#     number = ""
#     for i in el:
#         if i.isdigit():
#             number += i
#     numbers.append(number)
# int_num = [int(num) for num in numbers]
# char_num = [chr(num) for num in int_num]
# for chr in char_num:
#     counter +=1
#     if counter == 1:
#         str1 = chr
#     elif counter == 2:
#         str2 = chr
#     elif counter == 3:
#         str3 = chr
#     elif counter == 4:
#         str4 = chr
#     elif counter == 5:
#         str5 = chr
#     elif counter == 6:
#         str6 = chr
#
# for el in secret_message:
#     counter2 += 1
#     for i in el:
#         if i.isalpha():
#             if counter2 == 1:
#                 str1 = [str(x) for x in str1]
#                 str1.append(i)
#             elif counter2 == 2:
#                 str2 = [str(x) for x in str2]
#                 str2.append(i)
#             elif counter2 == 3:
#                 str3 = [str(x) for x in str3]
#                 str3.append(i)
#             elif counter2 == 4:
#                 str4 = [str(x) for x in str4]
#                 str4.append(i)
#             elif counter2 == 5:
#                 str5 = [str(x) for x in str5]
#                 str5.append(i)
#             elif counter2 == 6:
#                 str6 = [str(x) for x in str6]
#                 str6.append(i)
#
#
# str1[1], str1[-1] = str1[-1], str1[1]
# decipher.append("".join(str1))
# str2[1], str2[-1] = str2[-1], str2[1]
# decipher.append("".join(str2))
# str3[1], str3[-1] = str3[-1], str3[1]
# decipher.append("".join(str3))
# if len(secret_message) >= 4:
#     str4[1], str4[-1] = str4[-1], str4[1]
#     decipher.append("".join(str4))
# if len(secret_message) >= 5:
#     str5[1], str5[-1] = str5[-1], str5[1]
#     decipher.append("".join(str5))
# if len(secret_message) == 6:
#     str6[1], str6[-1] = str6[-1], str6[1]
#     decipher.append("".join(str6))
#
# print(" ".join(decipher))


secret_message = input().split()

for word in secret_message:
    result = []
    numbers_in_message = [i for i in word if i.isdigit()]
    numbers_as_ascii = chr(int("".join(numbers_in_message)))
    result += numbers_as_ascii
    letters_in_message = [i for i in word if i.isalpha()]
    result += letters_in_message
    result[1], result[-1] = result[-1], result[1]
    print("".join(result), end=" ")