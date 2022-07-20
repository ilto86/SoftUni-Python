# string = input()
# data = input()
#
# while data != "Generate":
#     command = data.split(">>>")
#
#     if command[0] == "Contains":
#         substring = command[1]
#         if substring in string:
#             print(f"{string} contains {substring}")
#         else:
#             print("Substring not found!")
#
#     elif command[0] == "Flip":
#         if command[1] == "Upper":
#             start_index = int(command[2])
#             end_index = int(command[3])
#             string = string[:start_index] + string[start_index :end_index].upper() + string[end_index:]
#             print(string)
#         else:
#             start_index = int(command[2])
#             end_index = int(command[3])
#             string = string[:start_index] + string[start_index :end_index].lower() + string[end_index:]
#             print(string)
#
#     elif command[0] == "Slice":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         string = string[start_index:] + string[end_index:]
#         print(string)
#
#     data = input()
#
# print(f"Your activation key is: {string}")




# activation_key = input()
#
# while True:
#     data = input()
#
#     if data == "Generate":
#         break
#
#     commands = data.split(">>>")
#     command = commands[0]
#
#     if command == "Contains":
#         substring = commands[1]
#         if substring in activation_key:
#             print(f"{activation_key} contains {substring}")
#         else:
#             print("Substring not found!")
#     if command == "Flip":
#         change_case = commands[1]
#         start_index = int(commands[2])
#         end_index = int(commands[3])
#         if change_case == "Upper":
#             activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + activation_key[end_index:]
#             print(activation_key)
#         else:
#             activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]
#             print(activation_key)
#     if command == "Slice":
#         start_index = int(commands[1])
#         end_index = int(commands[2])
#         if start_index < len(activation_key) and end_index < len(activation_key):
#             activation_key = activation_key[:start_index]  + activation_key[end_index:]
#             print(activation_key)
#
# print(f"Your activation key is: {activation_key}")




key = input()

while True:
    data = input()

    if data == "Generate":
        break

    command = data.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        action = command[1]
        start = int(command[2])
        end = int(command[3])
        if action == "Upper":
            key = key[:start] + key[start:end].upper() + key[end:]
            print(key)
        else:
            key = key[:start] + key[start:end].lower() + key[end:]
            print(key)

    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        key = key[:start] + key[end:]
        print(key)

print(f"Your activation key is: {key}")