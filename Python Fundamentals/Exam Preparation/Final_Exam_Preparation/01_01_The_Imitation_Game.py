# def move(message, num):
#     part_to_move = message[:num]
#     message = message + part_to_move
#     message = message.replace(part_to_move, '', 1)
#     return message
#
#
# def insert(message, idx, val):
#     message = list(message)
#     message.insert(idx, val)
#     return ''.join(message)
#
#
# encrypted_message = input()
#
# while True:
#     command = input().split("|")
#     action = command[0]
#     if action == 'Decode':
#         break
#
#     if action == "Move":
#         n_letters = int(command[1])
#         encrypted_message = move(encrypted_message, n_letters)
#
#     elif action == "Insert":
#         index = int(command[1])
#         value = command[2]
#         encrypted_message = insert(encrypted_message, index, value)
#
#     elif action == "ChangeAll":
#         subst = command[1]
#         replace = command[2]
#         encrypted_message = encrypted_message.replace(subst, replace)
#
# print(f"The decrypted message is: {encrypted_message}")




# message = input()
#
# operation = input()
#
# while not operation == "Decode":
#     command = operation.split("|")[0]
#
#     if command == "Move":
#         n_letters = int(operation.split("|")[1])
#         add_letter = message[:n_letters]
#         message = message[n_letters:] + add_letter
#
#     elif command == "Insert":
#         index = int(operation.split("|")[1])
#         value = operation.split("|")[2]
#         message = message[:index] + value + message[index:]
#
#     elif command == "ChangeAll":
#         substring, replacement = operation.split("|")[1:]
#         message = message.replace(substring, replacement)
#
#     operation = input()
#
# print(f"The decrypted message is: {message}")




# message = input()
#
# command = input()
#
# while command != "Decode":
#     command_params = command.split("|")
#
#     if command_params[0] == "Move":
#         location = int(command_params[1])
#         movement = message[:location]
#         static = message[location:]
#
#         message = static + movement
#
#     elif command_params[0] == "Insert":
#         index = int(command_params[1])
#         value = command_params[2]
#         before = message[:index]
#         after = message[index:]
#
#         message = before + value + after
#
#     elif command_params[0] == "ChangeAll":
#         current_substr = command_params[1]
#         replacement = command_params[2]
#
#         message = message.replace(current_substr, replacement)
#
#     command = input()
#
# print(f"The decrypted message is: {message}")




encrypted_message = input()

while True:
    data = input()
    if data == "Decode":
        break
    commands = data.split('|')
    command = commands[0]
    if command == "Move":
        number_of_letters = int(commands[1])
        letters = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters:] + letters
    elif command == "Insert":
        index = int(commands[1])
        value = commands[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command == "ChangeAll":
        substring = commands[1]
        replacement = commands[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")