# string = input()
# new_string = ""
# while True:
#     data = input()
#
#     if data == "Done":
#         break
#
#     commands = data.split()
#     command = commands[0]
#
#     if command == "TakeOdd":
#         count = 0
#         for char in string:
#             if count % 2 != 0:
#                 new_string += char
#             count += 1
#         string = new_string
#         print(string)
#     elif command == "Cut":
#         start = int(commands[1])
#         end = int(commands[2])
#         string = string[:start] + string[start + end:]
#         print(string)
#     elif command == "Substitute":
#         old = commands[1]
#         new = commands[2]
#         if old in string:
#             string = string.replace(old, new)
#             print(string)
#         else:
#             print("Nothing to replace!")
#
# print(f"Your password is: {string}")






# def take_odd(initial_text):
#     new_pass = ''
#     for i in range(1, len(initial_text), 2):
#         new_pass += initial_text[i]
#     return new_pass
#
#
# def cut(initial_text, idx, length):
#     new_pass = initial_text[:idx] + initial_text[idx + length:]
#     return new_pass
#
#
# def substitute(initial_text, subtxt, substit):
#     if subtxt in initial_text:
#         initial_text = initial_text.replace(subtxt, substit)
#         print(f"{initial_text}")
#         return initial_text
#
#     print(f"Nothing to replace!")
#     return initial_text
#
#
# password_text = input()
#
# while True:
#     command = input().split()
#
#     if command[0] == "Done":
#         break
#
#     if command[0] == "TakeOdd":
#         password_text = take_odd(password_text)
#         print(f"{password_text}")
#
#     elif command[0] == "Cut":
#         index = int(command[1])
#         length = int(command[2])
#         password_text = cut(password_text, index, length)
#         print(f"{password_text}")
#
#     elif command[0] == "Substitute":
#         subtext = command[1]
#         substit = command[2]
#         password_text = substitute(password_text, subtext, substit)
#
# print(f"Your password is: {password_text}")






# def take_odd(text: str):
#     result = ''
#     for i in range(len(text)):
#         if not i % 2 == 0:
#             result += text[i]
#     if result:
#         print(result)
#         return result
#     return text
#
#
# def cut(text: str, start: int, end: int):
#     sub_str = text[start:start + end]
#     start = text.find(sub_str)
#     result = text[:start] + text[start + end:]
#     print(result)
#     return result
#
#
# def substitute(text: str, sub_str: str, replacement: str):
#     if sub_str in text:
#         text = text.replace(sub_str, replacement)
#         print(text)
#     else:
#         print("Nothing to replace!")
#     return text
#
#
# password = input()
# command = input()
# while not command == 'Done':
#     command = command.split()
#     if command[0] == 'TakeOdd':
#         password = take_odd(password)
#     elif command[0] == 'Cut':
#         password = cut(password, int(command[1]), int(command[2]))
#     elif command[0] == 'Substitute':
#         password = substitute(password, command[1], command[2])
#     command = input()
# print(f"Your password is: {password}")




string = input()

while True:
    data = input()
    if data == "Done":
        break

    command = data.split()

    if command[0] == 'TakeOdd':
        new_password = ""
        index = 0
        for char in string:
            if index % 2 == 0:
                index += 1
                continue
            else:
                new_password += char
                index += 1
        string = new_password
        print(string)

    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        string = string[:index] + string[index + length:]
        print(string)

    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {string}")