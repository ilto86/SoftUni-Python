# import re
# from re import split
#
# EXPRESSION = "[&&<>]"
#
# def read_string_input():
#     END = "find"
#     result = []
#
#     while True:
#         text = input()
#
#         if text == END:
#             break
#
#         result.append(text)
#
#     return result
#
# def get_char_and_key_number(string, key, char_index, key_num_index):
#     char = string[char_index]
#     key_num = key[key_num_index]
#
#     return char, key_num
#
# def decrease_ascii_code_of_char(char, key_num):
#     result = chr(ord(char) - key_num)
#     return result
#
#
# def format_message(msg):
#     split_msg = re.split(EXPRESSION, msg)
#     treasure_type = split_msg[1]
#     coordinates = split_msg[3]
#
#     return f"Found {treasure_type} at {coordinates}"
#
# def decrypt_string(string, key):
#     num_index = 0
#     message = ""
#
#     for i in range(len(string)):
#
#         if num_index == len(key):
#             num_index = 0
#
#         char, key_num = get_char_and_key_number(string, key, i, num_index)
#         char = decrease_ascii_code_of_char(char, key_num)
#         message += char
#         num_index += 1
#
#     return message
#
# key = list(map(int, input().split()))
# strings = read_string_input()
#
# for string in strings:
#     decrypted_message = decrypt_string(string, key)
#     print(format_message(decrypted_message))







# from itertools import cycle
# KEYS = [int(n) for n in input().strip().split()]
#
#
# def decrypt_line(text):
# 	decrypted = ""
# 	index = 0
# 	for key in cycle(KEYS):
# 		decrypted += chr(ord(text[index]) - key)
# 		index += 1
# 		if index == len(text):
# 			return decrypted
#
#
# def get_info(msg):
# 	start_treasure, stop_treasure = [index for index, char in enumerate(msg) if char == "&"]
# 	start_coordinates, stop_coordinates = msg.index("<"), msg.index(">")
# 	return msg[start_treasure+1:stop_treasure], msg[start_coordinates+1:stop_coordinates]
#
#
# line = input()
# while not line == "find":
# 	message = decrypt_line(line)
# 	treasure, coordinates = get_info(message)
# 	print(f"Found {treasure} at {coordinates}")
# 	line = input()






# import itertools
#
# key_sequence = list(map(int, input().split()))
#
# final_text = ''
#
# while True:
#
#     text = input()
#     if text == "find":
#         break
#
#     for value, key in zip(text, itertools.cycle(key_sequence)):
#         current_value = ord(value) - key
#         final_text += chr(current_value)
#
#     start = final_text.find('&') + 1
#     end = final_text.find('&', start)
#     treasure = final_text[start:end]
#     start = final_text.find('<') + 1
#     end = final_text.find('>', start)
#     coordinates = final_text[start:end]
#     print(f"Found {treasure} at {coordinates}")
#     final_text = ''





key = [int(x) for x in input().split()]
text = input()
while not text == 'find':
    index = 0
    tmp_text = ''
    for el in text:
        tmp_text += chr(ord(el) - key[index])
        index += 1
        if index == len(key):
            index = 0
    name = tmp_text[tmp_text.index('&') + 1: tmp_text.rindex('&')]
    position = tmp_text[tmp_text.index('<') + 1: tmp_text.index('>')]
    print(f'Found {name} at {position}')
    text = input()