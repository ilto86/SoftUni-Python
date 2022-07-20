first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    command_parts = input().split()
    command = command_parts[0]
    target_set = command_parts[1]

    if command == "Add":
        if target_set == "First":
            # Add First 1 2 3
            first = first.union([int(x) for x in command_parts[2:]])
        else:
            # Add Second 1 2 3
            second = second.union([int(x) for x in command_parts[2:]])
    elif command == "Remove":
        if target_set == "First":
            # Remove First 1 2 3
            first = first.difference([int(x) for x in command_parts[2:]])
        else:
            # Remove Second 1 2 3
            second = second.difference([int(x) for x in command_parts[2:]])
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")





# first_sequences = {int(x) for x in input().split()}
# second_sequences = {int(x) for x in input().split()}
# n = int(input())
#
# for _ in range(n):
#     line = input().split()
#     command = line[0]
#     sequence = line[1]
#
#     if command == "Add":
#         if sequence == "First":
#             [first_sequences.add(int(x)) for x in line[2:]]
#         else:
#             [second_sequences.add(int(x)) for x in line[2:]]
#     elif command == "Remove":
#         if sequence == "First":
#             first_sequences = first_sequences.difference([int(x) for x in line[2:]])
#         else:
#             second_sequences = second_sequences.difference([int(x) for x in line[2:]])
#     else:
#         print(first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences))
#
# print(*sorted(first_sequences), sep=", ")
# print(*sorted(second_sequences), sep=", ")








# first_sequences = {int(x) for x in input().split()}
# second_sequences = {int(x) for x in input().split()}
# n = int(input())
#
# for _ in range(n):
#     line = input().split()
#     command = line[0]
#     sequence = line[1]
#
#     if command == "Add":
#         if sequence == "First":
#             for idx in range(len(line)):
#                 if line[idx].isdigit():
#                     num = int(line[idx])
#                     first_sequences.add(num)
#         else:
#             for idx in range(len(line)):
#                 if line[idx].isdigit():
#                     num = int(line[idx])
#                     second_sequences.add(num)
#
#     elif command == "Remove":
#         if sequence == "First":
#             for idx in range(len(line)):
#                 if line[idx].isdigit():
#                     num = int(line[idx])
#                     if num in first_sequences:
#                         first_sequences.remove(num)
#         else:
#             for idx in range(len(line)):
#                 if line[idx].isdigit():
#                     num = int(line[idx])
#                     if num in second_sequences:
#                         second_sequences.remove(num)
#
#     else:
#         if first_sequences.issubset(second_sequences):
#             print(True)
#         elif second_sequences.issubset(first_sequences):
#             print(True)
#         else:
#             print(False)
#
# print(*sorted(first_sequences), sep=", ")
# print(*sorted(second_sequences), sep=", ")
