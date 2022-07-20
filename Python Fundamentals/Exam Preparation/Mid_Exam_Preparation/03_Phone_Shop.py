# phone_list = input().split(", ")
# command = input()
#
# while command != "End":
#     current_command = command.split(" - ")
#
#     if current_command[0] == "Add":
#         item = current_command[1]
#         if item not in phone_list:
#             phone_list.append(item)
#     elif current_command[0] == "Remove":
#         item = current_command[1]
#         if item in phone_list:
#             phone_list.remove(item)
#     if current_command[0] == "Bonus phone":
#         item = current_command[1]
#         old_item = item.split(":")[0]
#         new_item = item.split(":")[1]
#         if old_item in phone_list:
#             idx = phone_list.index(old_item)
#             phone_list.insert(idx + 1, new_item)
#     if current_command[0] == "Last":
#         item = current_command[1]
#         if item in phone_list:
#             phone_list.remove(item)
#             phone_list.append(item)
#
#     command = input()
#
# new_phone_list = ", ".join(phone_list)
# print(new_phone_list)





phone_list = input().split(", ")

while True:
    command = input()

    if command == "End":
        break

    current_command = command.split(" - ")
    action = current_command[0]
    item = current_command[1]

    if action == "Add":
        if item not in phone_list:
            phone_list.append(item)

    elif action == "Remove":
        item = current_command[1]
        if item in phone_list:
            phone_list.remove(item)

    elif action == "Bonus phone":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in phone_list:
            idx = phone_list.index(old_item)
            phone_list.insert(idx + 1, new_item)

    elif action == "Last":
        if item in phone_list:
            phone_list.remove(item)
            phone_list.append(item)

print(f"{', '.join(phone_list)}")