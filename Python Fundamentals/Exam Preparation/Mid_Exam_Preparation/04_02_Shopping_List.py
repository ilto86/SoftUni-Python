# list = input().split("!")
# command = input()
#
# while command != "Go Shopping!":
#     current_command = command.split()
#
#     if current_command[0] == "Urgent" and not current_command[1] in list:
#             list.insert(0, current_command[1])
#
#     if current_command[0] == "Unnecessary" and current_command[1] in list:
#             list.remove(current_command[1])
#
#     if current_command[0] == "Correct" and current_command[1] in list:
#         current_index = list.index(current_command[1])
#         list[current_index] = current_command[2]
#
#     if current_command[0] == "Rearrange" and current_command[1] in list:
#             list.remove(current_command[1])
#             list.append(current_command[1])
#
#     command = input()
#
# new_list = ", ".join(list)
# print(new_list)





initial_list = [text for text in input().split("!")]

while True:
    data = input()

    if data == "Go Shopping!":
        break

    commands = data.split()
    command = commands[0]
    item = commands[1]

    if command == "Urgent" and item not in initial_list:
        initial_list.insert(0, item)

    elif command == "Unnecessary" and item in initial_list:
        initial_list.remove(item)

    elif command == "Correct" and item in initial_list:
        new_item = commands[2]
        index = initial_list.index(item)
        initial_list[index] = new_item

    elif command == "Rearrange" and item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)

print(", ".join(initial_list))