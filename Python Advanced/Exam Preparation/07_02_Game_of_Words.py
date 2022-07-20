def is_inside(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


text = input()
size = int(input())
field = []
player_row = 0
player_col = 0

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    row_element = [x for x in input()]
    for col in range(size):
        if row_element[col] == "P":
            player_row = row
            player_col = col
    field.append(row_element)

n = int(input())
for _ in range(n):
    field[player_row][player_col] = "-"
    move_command = input()
    move_position = moves[move_command]
    next_row, next_col = player_row + move_position[0], player_col + move_position[1]

    if is_inside(next_row, next_col, size):
        if field[next_row][next_col].isalpha():
            text += field[next_row][next_col]
            field[next_row][next_col] = "-"
            player_row, player_col = next_row, next_col
        elif field[next_row][next_col] == "-":
            field[next_row][next_col] = "-"
            player_row, player_col = next_row, next_col
    else:
        text = text[:-1]

field[player_row][player_col] = "P"

print(text)
for row in field:
    print(*row, sep="")