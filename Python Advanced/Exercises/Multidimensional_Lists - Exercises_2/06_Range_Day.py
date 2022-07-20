# size = 5
# matrix = []
#
# player_row = 0
# player_col = 0
# targets = 0
#
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == "A":
#             player_row = row
#             player_col = col
#         elif row_elements[col] == "x":
#             targets += 1
#     matrix.append(row_elements)
#
# n = int(input())
# hit_targets = []
#
# def get_next_pos(player_row, player_col, direction, steps):
#     if direction == "up":
#         return player_row - steps, player_col
#     if direction == "down":
#         return player_row + steps, player_col
#     if direction == "left":
#         return player_row, player_col - steps
#     if direction == "right":
#         return player_row, player_col + steps
#
#
# def is_inside(next_row, next_col, size):
#     return 0 <= next_row < size and 0 <= next_col < size
#
# matrix[player_row][player_col] = "."
#
# for _ in range(n):
#     command_parts = input().split()
#     command = command_parts[0]
#     direction = command_parts[1]
#
#     if command == "move":
#         steps = int(command_parts[2])
#         next_row, next_col = get_next_pos(player_row, player_col, direction, steps)
#
#         if is_inside(next_row, next_col, size) and matrix[next_row][next_col] == ".":
#             player_row, player_col = next_row, next_col
#
#     else: # elif command == "shoot":
#         bullet_row, bullet_col = get_next_pos(player_row, player_col, direction, 1)
#         while is_inside(bullet_row, bullet_col, size):
#             if matrix[bullet_row][bullet_col] == "x":
#                 targets -= 1
#                 matrix[bullet_row][bullet_col] = "."
#                 hit_targets.append([bullet_row, bullet_col])
#                 break
#             bullet_row, bullet_col = get_next_pos(bullet_row, bullet_col, direction, 1)
#         if targets == 0:
#             break
#
# if targets == 0:
#     print(f"Training completed! All {len(hit_targets)} targets hit.")
# else:
#     print(f"Training not completed! {targets} targets left.")
#
# print(*hit_targets, sep="\n")






def get_direc(direction, row, col, len):
    if direction == "right":
        return row, col + len
    if direction == "left":
        return row, col - len
    if direction == "up":
        return row - len, col
    if direction == "down":
        return row + len, col

size = 5
matrix = []

player_row = 0
player_col = 0
targets = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "A":
            player_row = row
            player_col = col
        if row_elements[col] == "x":
            targets += 1
    matrix.append(row_elements)

command_count = int(input())

matrix[player_row][player_col] = "."
targets_hit = []
for _ in range(command_count):
    commands = input().split()
    command = commands[0]
    direction = commands[1]

    if command == "move":
        lenght = int(commands[2])
        next_row, next_col = get_direc(direction, player_row, player_col, lenght)

        if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size or matrix[next_row][next_col] == "x":
            continue

        player_row, player_col = next_row, next_col

    else:
        lenght = 1
        bullet_row, bullet_col = get_direc(direction, player_row, player_col, lenght)

        while bullet_row >= 0 and bullet_row < size and bullet_col >= 0 and bullet_col < size:
            if matrix[bullet_row][bullet_col] == "x":
                targets -= 1
                targets_hit.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = "."
                break
            bullet_row, bullet_col = get_direc(direction, bullet_row, bullet_col, lenght)

        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {len(targets_hit)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

for el in targets_hit:
    print(el)