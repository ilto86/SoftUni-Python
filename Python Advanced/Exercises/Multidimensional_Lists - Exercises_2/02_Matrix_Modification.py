# size = int(input())
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])
#
# while True:
#     line = input()
#     if line == "END":
#         break
#
#     parts = line.split()
#     command = parts[0]
#     row, col, value = [int(x) for x in parts[1:]]
#
#     if row < 0 or col < 0 or row >= size or col >= size:
#         print("Invalid coordinates")
#         continue
#
#     if command == "Add":
#         matrix[row][col] += value
#     else:
#         matrix[row][col] -= value
#
# for row in matrix:
#     print(*row, sep=' ')




rows_cols = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_cols)]

while True:
    commands = input().split()
    command = commands[0]
    if command == "END":
        break

    row, col, value = int(commands[1]), int(commands[2]), int(commands[3])

    if 0 <= row < rows_cols and 0 <= col < rows_cols:
        if command == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for el in matrix:
    print(*el)