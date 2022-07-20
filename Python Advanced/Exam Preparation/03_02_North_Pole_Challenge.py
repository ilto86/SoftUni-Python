# def is_outside(row, col, horizontal_size, vertical_size):
#     if row < 0:
#         return horizontal_size - 1, col
#     elif row >= horizontal_size:
#         return 0, col
#     elif col < 0:
#         return row, vertical_size - 1
#     elif col >= vertical_size:
#         return row, 0
#
#
# rows_size, cols_size = [int(x) for x in input().split(", ")]
# matrix = []
#
# player_row = 0
# player_col = 0
# all_items = 0
# collected_all_items = False
#
# for row in range(rows_size):
#     row_element = input().split()
#     for col in range(cols_size):
#         if row_element[col] == "Y":
#             player_row = row
#             player_col = col
#         elif row_element[col] == "D" or row_element[col] == "G" or row_element[col] == "C":
#             all_items += 1
#     matrix.append(row_element)
#
# christmas_decorations = 0
# gifts = 0
# cookies = 0
#
# moves = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1)
# }
#
# while True:
#     action = input()
#
#     if action == "End":
#         break
#
#     direction, steps = action.split("-")
#     move_position = moves[direction]
#
#     for _ in range(int(steps)):
#         matrix[player_row][player_col] = "x"
#         next_row, next_col = player_row + move_position[0], player_col + move_position[1]
#
#         if next_row < 0 or next_row >= rows_size or next_col < 0 or next_col >= cols_size:
#             next_row, next_col = is_outside(next_row, next_col, rows_size, cols_size)
#
#         if matrix[next_row][next_col] == "D":
#             christmas_decorations += 1
#             all_items -= 1
#             matrix[next_row][next_col] = "x"
#             player_row, player_col = next_row, next_col
#         if matrix[next_row][next_col] == "G":
#             gifts += 1
#             all_items -= 1
#             matrix[next_row][next_col] = "x"
#             player_row, player_col = next_row, next_col
#         if matrix[next_row][next_col] == "C":
#             cookies += 1
#             all_items -= 1
#             matrix[next_row][next_col] = "x"
#             player_row, player_col = next_row, next_col
#
#         if all_items == 0:
#             collected_all_items = True
#             break
#
#         player_row, player_col = next_row, next_col
#
#     if collected_all_items:
#         break
#
# matrix[player_row][player_col] = "Y"
# if collected_all_items:
#     print("Merry Christmas!")
#
# print("You've collected:")
# print(f"- {christmas_decorations} Christmas decorations")
# print(f"- {gifts} Gifts")
# print(f"- {cookies} Cookies")
#
# for row in matrix:
#     print(*row, sep=" ")





def is_outside(row, col, horizontal_size, vertical_size):
    if row < 0:
        return horizontal_size - 1, col
    elif row >= horizontal_size:
        return 0, col
    elif col < 0:
        return row, vertical_size - 1
    elif col >= vertical_size:
        return row, 0


rows, cols = [int(x) for x in input().split(", ")]
matrix = []
player_row = 0
player_col = 0
christmas_decorations = 0
gifts = 0
cookies = 0

for row in range(rows):
    row_elements = [x for x in input().split()]
    for col in range(cols):
        if row_elements[col] == "Y":
            player_row = row
            player_col = col
        elif row_elements[col] == "D":
            christmas_decorations += 1
        elif row_elements[col] == "G":
            gifts += 1
        elif row_elements[col] == "C":
            cookies += 1

    matrix.append(row_elements)

all_items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0
}
directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}

current_row, current_col = player_row, player_col
matrix[current_row][current_col] = "x"
merry_christmas = False

while not merry_christmas:
    action = input()

    if action == "End":
        break

    command = action.split("-")
    direction, steps = command[0], int(command[1])
    next_row, next_col = current_row, current_col

    for step in range(steps):
        next_row, next_col = current_row + directions[direction][0], current_col + directions[direction][1]

        if 0 > next_row or next_row >= rows or 0 > next_col or next_col >= cols:
            next_row, next_col = is_outside(next_row, next_col, rows, cols)

        if matrix[next_row][next_col] == "D":
            christmas_decorations -= 1
            all_items["Christmas decorations"] += 1

        if matrix[next_row][next_col] == "G":
            gifts -= 1
            all_items["Gifts"] += 1

        if matrix[next_row][next_col] == "C":
            cookies -= 1
            all_items["Cookies"] += 1

        matrix[next_row][next_col] = "x"
        current_row, current_col = next_row, next_col

        if not christmas_decorations and not gifts and not cookies:
            merry_christmas = True
            break

matrix[current_row][current_col] = "Y"
if merry_christmas:
    print("Merry Christmas!")

print("You've collected:")
for key, value in all_items.items():
    print(f"- {value} {key}")

for r in matrix:
    print(*r, sep=" ")