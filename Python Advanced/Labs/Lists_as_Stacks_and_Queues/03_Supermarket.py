# from collections import deque
#
# name = input()
# line = deque()
#
# while not name == "End":
#     if name == "Paid":
#         while line:
#             print(line.popleft())
#     else:
#         line.append(name)
#     name = input()
#
# print(f"{len(line)} people remaining.")






from collections import deque

command = input()
queue = deque()

while not command == "End":
    if command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)

    command = input()

print(f"{len(queue)} people remaining.")