# size = int(input())
#
# matrix = []
# bunny_row = 0
# bunny_col = 0
#
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == "B":
#             bunny_row = row
#             bunny_col = col
#     matrix.append(row_elements)
#
# directions = {
#     "down": lambda r, c: (r + 1, c),
#     "left": lambda r, c: (r, c - 1),
#     "up": lambda r, c: (r - 1, c ),
#     "right": lambda r, c: (r, c + 1),
# }
#
# best_sum = float("-inf")
# best_dir = ""
# best_path = []
#
# for direction in directions:
#     # print(f"Direction: {direction}")
#     current_sum = 0
#     row, col = directions[direction](bunny_row, bunny_col)
#     current_path = []
#
#     while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
#         current_sum += int(matrix[row][col])
#         current_path.append([row, col])
#         row, col = directions[direction](row, col)
#     # print(f"Direction: {direction}; Sum: {current_sum}")
#     if current_sum > best_sum and current_path:
#         best_sum = current_sum
#         best_dir = direction
#         best_path = current_path
#
# print(best_dir)
# print(*best_path, sep="\n")
# print(best_sum)




size = int(input())
matrix = []

bunny_row = 0
bunny_col = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "B":
            bunny_row = row
            bunny_col = col
    matrix.append(row_elements)

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1)
}

max_sum = -99999999
max_direction = ""
max_path = []

for direction in directions:
    current_sum = 0
    row, col = directions[direction](bunny_row, bunny_col)
    current_path = []

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
        current_sum += int(matrix[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

        if current_sum > max_sum:
            max_sum = current_sum
            max_path = current_path
            max_direction = direction

print(max_direction)
print(*max_path, sep="\n")
print(max_sum)