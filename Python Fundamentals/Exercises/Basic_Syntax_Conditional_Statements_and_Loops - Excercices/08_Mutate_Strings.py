# first_string = input()
# second_string = input()
# last_string = first_string
# for symbol in range(len(first_string)):
#     left_part = second_string[:symbol + 1]
#     right_part = first_string[symbol + 1:]
#     current_string = left_part + right_part
#     if current_string == last_string:
#         continue
#     print(current_string)
#     last_string = current_string


# first_string = input()
# second_string = input()
# new_word = ""
# for i in range(1, len(first_string) + 1):
#     a_letter = ord(first_string[i - 1])
#     b_letter = ord(second_string[i - 1])
#     if a_letter != b_letter:
#         new_word = second_string[:i] + first_string[i:]
#         print(new_word)


# word1 = str(input())
# word2 = str(input())
# for i in range(len(word1)):
#     if word1[i] != word2[i]:
#         word1 = word1.replace(word1[i], word2[i])
#         print(word1)
#     else:
#         print(word1)


# text1 = input()
# text2 = input()
#
# text1_list = list(text1)
#
# for i in range(len(text1)):
#     if text1[i] != text2[i]:
#         text1_list[i] = text2[i]
#         result = "".join(text1_list)
#         print(result)

first_word = input()
second_word = input()

for i in range(len(first_word)):
    if first_word[i] != second_word[i]:
        replacement = second_word[i]
        word = first_word[0:i] + replacement + first_word[i + 1:]
        first_word = word
        print(first_word)