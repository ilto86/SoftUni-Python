# destination = input()
#
#
# while True:
#     data = input()
#
#     if data == "Travel":
#         break
#
#     command = data.split(":")
#
#     if command[0] == "Add Stop":
#         index = int(command[1])
#         add_place = command[2]
#         if 0 <= index < len(destination):
#             destination = destination[0: index:] + add_place + destination[index:]
#         print(destination)
#
#     elif command[0] == "Remove Stop":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         if 0 <= start_index < len(destination) and 0 <= end_index < len(destination):
#             destination = destination[0: start_index:] + destination[end_index+1:]
#         print(destination)
#
#     elif command[0] == "Switch":
#         old_place = command[1]
#         new_place = command[2]
#         destination = destination.replace(old_place, new_place)
#         print(destination)
#
# print(f"Ready for world tour! Planned stops: {destination}")










# def world_tour(destinations):
#
#     while True:
#         command = input().split(":")
#
#         if command[0] == "Travel":
#             print(f"Ready for world tour! Planned stops: {destinations}")
#             break
#
#         elif command[0] == "Add Stop":
#             index = int(command[1])
#             string = command[2]
#             if 0 <= index <= len(destinations):
#                 destinations = destinations[:index] + string + destinations[index:]
#         elif command[0] == "Remove Stop":
#             start_index = int(command[1])
#             end_index = int(command[2])
#             if 0 <= start_index <= end_index < len(destinations):
#                 destinations = destinations[:start_index] + destinations[end_index + 1:] # destination[:start_index:end_index+1:]
#         elif command[0] == "Switch":
#             old_string = command[1]
#             new_string = command[2]
#             if old_string in destinations:
#                 destinations = destinations.replace(old_string, new_string)
#
#         print(destinations)
#
# data = input()
# world_tour(data)




text = input()

while True:
    data = input()

    if data == "Travel":
        break

    commands = data.split(":")
    command = commands[0]

    if command == "Add Stop":
        index, string = int(commands[1]), commands[2]

        if 0 <= index < len(text):
            text = text[:index] + string + text[index:]
        print(text)

    elif command == "Remove Stop":
        start_index, end_index = int(commands[1]), int(commands[2])

        if 0 <= start_index <= end_index < len(text):
            text = text[:start_index] + text[end_index + 1:]
        print(text)

    elif command == "Switch":
        old_string, new_string = commands[1], commands[2]

        if old_string in text:
            text = text.replace(old_string, new_string)
        print(text)

print(f"Ready for world tour! Planned stops: {text}")