# Моето решението
# characters = input()
# new_chars = ""
#
# for char in characters:
#     new_chars += char
#     while char * 2 in new_chars:
#         new_chars = new_chars.replace(char * 2, char * 1)
#
# print(new_chars)





# Решението на Сашко
# text_data = input()
# text_list = [x for x in text_data]
#
# for index, char in enumerate(text_list):
#     if index + 1 >= len(text_list):
#         break
#     if text_list[index + 1] == char:
#         text_list[index] = ""
#
# print(''.join(text_list))




# text = input()
# correct_text = list(text)
# for index in range(len(text)-1, 0, -1):
# 	if text[index] == text[index-1]:
# 		correct_text.pop(index)
#
# print("".join(correct_text))




# characters = input()
# new_chars = ""
# result =""
#
# for char in characters:
#     if char != new_chars:
#         new_chars = char
#         result += char
#
# print(result)



text = input()
new_text = text[0]

for i in range(1, len(text)):
    if not text[i - 1] == text[i]:
        new_text += text[i]

print(new_text)
