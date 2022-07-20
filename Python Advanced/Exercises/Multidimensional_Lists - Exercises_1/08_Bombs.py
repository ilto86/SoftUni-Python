# def get_children(matrix, row, col):
#         possible_children_cords = [
#             [row - 1, col - 1],
#             [row - 1, col],
#             [row - 1, col + 1],
#             [row, col - 1],
#             [row, col + 1],
#             [row + 1, col - 1],
#             [row + 1, col],
#             [row + 1, col + 1],
#         ]
#
#         result = []
#         for child_row, child_col in possible_children_cords:
#             if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
#                 result.append([child_row, child_col])
#         return result
#
# size = int(input())
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])
#
# bombs = input().split()
#
# for bomb in bombs:
#     row, col = [int(x) for x in bomb.split(",")]
#     power = matrix[row][col]
#
#     if power <= 0:
#         continue
#
#     matrix[row][col] = 0
#
#     children = get_children(matrix, row, col)
#     for child_row, child_col in children:
#         matrix[child_row][child_col] -= power
#
# alive_cells_count = 0
# alive_cells_sums = 0
#
# for row in matrix:
#     for el in row:
#         if el > 0:
#             alive_cells_count += 1
#             alive_cells_sums += el
#
# print(f"Alive cells: {alive_cells_count}")
# print(f"Sum: {alive_cells_sums}")
# for row in matrix:
#     print(*row)






def get_children(matrix, row, col):
    possible_children_cords = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1],
    ]

    result = []
    for child_row, child_col in possible_children_cords:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result

size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(",")]
    power = matrix[row][col]

    if power <= 0:
        continue

    children = get_children(matrix, row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power

alive_cells_count = 0
alive_cells_sums = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells_count += 1
            alive_cells_sums += el

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sums}")
for row in matrix:
    print(*row)








# def is_inside(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
# def get_neighbours(row, col, matrix):
#     size = len(matrix)
#     neighbours = []
#     # row - 1, col
#     if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
#         neighbours.append([row - 1, col])
#     # row + 1, col
#     if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
#         neighbours.append([row + 1, col])
#     # row, col - 1
#     if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
#         neighbours.append([row, col - 1])
#     # row, col + 1
#     if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
#         neighbours.append([row, col + 1])
#     # row - 1, col - 1
#     if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
#         neighbours.append([row - 1, col - 1])
#     # row - 1, col + 1
#     if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
#         neighbours.append([row - 1, col + 1])
#     # row + 1, col - 1
#     if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
#         neighbours.append([row + 1, col - 1])
#     # row + 1, col + 1
#     if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
#         neighbours.append([row + 1, col + 1])
#     return  neighbours
#
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(x) for x in input().split()])
#
# bombs = input().split()
#
# for bomb_cords in bombs:
#     bomb_row, bomb_col = [int(x) for x in bomb_cords.split(",")]
#     if matrix[bomb_row][bomb_col] <= 0:
#         continue
#
#     bomb_power = matrix[bomb_row][bomb_col]
#     neighbours = get_neighbours(bomb_row, bomb_col, matrix)
#
#     matrix[bomb_row][bomb_col] = 0
#
#     for row, col in neighbours:
#         matrix[row][col] -= bomb_power
#
# alive_cells = 0
# alive_cells_sum = 0
# for row in matrix:
#     for el in row:
#         if el > 0:
#             alive_cells += 1
#             alive_cells_sum += el
#
# print(f"Alive cells: {alive_cells}")
# print(f"Sum: {alive_cells_sum}")
# for row in matrix:
#     print(*row, sep=" ")










# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(x) for x in input().split()])
#
# bombs = input().split()
#
# for bomb_cords in bombs:
#     bomb_row, bomb_col = [int(x) for x in bomb_cords.split(",")]
#     if matrix[bomb_row][bomb_col] <= 0:
#         continue
#
#     bomb_power = matrix[bomb_row][bomb_col]
#
#     matrix[bomb_row][bomb_col] = 0
#
#     for row in range(bomb_row - 1, bomb_row + 2):
#         for col in range(bomb_col - 1, bomb_col + 2):
#             if 0 <= row < n and 0 <= col < n and matrix[row][col] > 0:
#                 matrix[row][col] -= bomb_power
#
# alive_cells = 0
# alive_cells_sum = 0
# for row in matrix:
#     for el in row:
#         if el > 0:
#             alive_cells += 1
#             alive_cells_sum += el
#
# print(f"Alive cells: {alive_cells}")
# print(f"Sum: {alive_cells_sum}")
# for row in matrix:
#     print(*row, sep=" ")