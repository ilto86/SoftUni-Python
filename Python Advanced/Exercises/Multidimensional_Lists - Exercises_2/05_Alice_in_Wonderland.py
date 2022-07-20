# def get_next_pos(row, col, direction):
#     if direction == "up":
#         return row - 1, col
#     if direction == "down":
#         return row + 1, col
#     if direction == "left":
#         return row, col - 1
#     if direction == "right":
#         return row, col + 1
#
# size = int(input())
# matrix = []
#
# alice_row = 0
# alice_col = 0
#
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == "A":
#             alice_row = row
#             alice_col = col
#     matrix.append(row_elements)
#
# tea_bags = 0
#
# while tea_bags < 10:
#     matrix[alice_row][alice_col] = "*"
#
#     direction = input()
#     next_row, next_col = get_next_pos(alice_row, alice_col, direction)
#
#     if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
#         break
#
#     alice_row, alice_col = next_row, next_col
#
#     if matrix[alice_row][alice_col] == "." or matrix[alice_row][alice_col] == "*":
#         continue
#     if matrix[alice_row][alice_col] == "R":
#         break
#
#     tea_bags += int(matrix[alice_row][alice_col])
#
# matrix[alice_row][alice_col] = "*"
#
# if tea_bags >= 10:
#     print("She did it! She went to the party. ")
# else:
#     print("Alice didn't make it to the tea party.")
#
# for row in matrix:
#     print(*row, sep=' ')




def get_position(command, row, col):
    if command == "up":
        return row - 1, col
    if command == "down":
        return row + 1, col
    if command == "left":
        return row, col - 1
    if command == "right":
        return row, col + 1

size = int(input())

matrix = []

alice_row = 0
alice_col = 0
tea_bags = 0

for row in range(size):
    row_element = input().split()
    for col in range(size):
        if row_element[col] == "A":
            alice_row = row
            alice_col = col
    matrix.append(row_element)

matrix[alice_row][alice_col] = "*"

while tea_bags < 10:
    command = input()
    next_row, next_col = get_position(command, alice_row, alice_col)

    if 0 > next_row or next_row >= size or 0 > next_col or next_col >= size:
        break

    if matrix[next_row][next_col] == "R":
        matrix[next_row][next_col] = "*"
        break

    alice_row, alice_col = next_row, next_col

    if matrix[next_row][next_col] == "." or matrix[next_row][next_col] == "*":
        matrix[next_row][next_col] = "*"
        continue

    tea_bags += int(matrix[next_row][next_col])
    matrix[next_row][next_col] = "*"

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=' ')