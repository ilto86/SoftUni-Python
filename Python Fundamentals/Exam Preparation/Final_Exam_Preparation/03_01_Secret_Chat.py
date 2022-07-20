# message = input()
#
# while True:
#     command = input()
#
#     if command == "Reveal":
#         break
#
#     commands = command.split(":|:")
#     operation = commands[0]
#
#     if operation == "InsertSpace":
#         index = int(commands[1])
#         message = message[:index] + " " + message[index:]
#         print(message)
#
#     elif operation == "Reverse":
#         word = commands[1]
#         new_word = word[::-1]
#         if word in message:
#             message = message.replace(word, "", 1)
#             message = message + new_word
#             print(message)
#         else:
#             print("error")
#
#     elif operation == "ChangeAll":
#         old_char = commands[1]
#         new_char = commands[2]
#         message = message.replace(old_char, new_char)
#         print(message)
#
# print(f"You have a new text message: {message}")





concealed_message = input()

while True:
    data = input()
    if data == "Reveal":
        break

    commands = data.split(":|:")
    command = commands[0]

    if command == "ChangeAll":
        substring, replacement = commands[1], commands[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    elif command == "Reverse":
        substring = commands[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            reversed_substring = substring[::-1]
            concealed_message = concealed_message + reversed_substring
            print(concealed_message)
        else:
            print("error")
    elif command == "InsertSpace":
        index = int(commands[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")