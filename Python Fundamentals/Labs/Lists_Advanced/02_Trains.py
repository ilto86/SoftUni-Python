# wagons = int(input())
# train_list = [0] * wagons # train = [0 for i in range(num_wagons)]
# command = input()

# while command != "End":
#     current_command = command.split()
#     if current_command[0] == "add":
#         add_people = int(current_command[1])
#         train_list[-1] += add_people  # train_list[len(train_list) -1] += add_people
#     elif current_command[0] == "insert":
#         insert_people_index = int(current_command[1])
#         insert_people = int(current_command[2])
#         train_list[insert_people_index] += insert_people
#     elif current_command[0] == "leave":
#         leave_people_index = int(current_command[1])
#         leave_people = int(current_command[2])
#         train_list[leave_people_index] -= leave_people

#     command = input()


# print(train_list)




train_list = [0] * int(input())
command = input()

while command != "End":

    current_list = command.split()

    if "add" in command:
        train_list[-1] += int(current_list[1])
    if "insert" in command:
        train_list[int(current_list[1])] += int(current_list[2])
    if "leave" in command:
        train_list[int(current_list[1])] -= int(current_list[2])

    command = input()

print(train_list)
