from math import floor

def is_outside(row, col, n):
        if row < 0:
            return n - 1, col
        elif row >= n:
            return 0, col
        elif col < 0:
            return row, n - 1
        elif col >= n:
            return row, 0


size = int(input())
field = []
player_position = []

for row in range(size):
    row_element = [x for x in input().split()]  # only digit in int(number): [int(x) if x.isdigit() else x for x in input().split()]
    for col in range(size):
        if row_element[col] == "P":
            player_position.append(row)
            player_position.append(col)

    field.append(row_element)

moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
game_won = False
your_path = []
player_row, player_col = player_position
coins = 0
your_path.append([player_row, player_col])
while not game_won:
    direction = input()

    if direction in moves:
        next_row, next_col = player_row + moves[direction][0], player_col + moves[direction][1]

        if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
            next_row, next_col = is_outside(next_row, next_col, size)

        if field[next_row][next_col] == "X":
            coins = coins / 2
            your_path.append([next_row, next_col])
            break

        if field[next_row][next_col].isdigit():
            coins += int(field[next_row][next_col])
            field[next_row][next_col] = "-"

        if coins >= 100:
            game_won = True

        player_row, player_col = next_row, next_col
        your_path.append([player_row, player_col])

if game_won:
    print(f"You won! You've collected {floor(coins)} coins.")
else:
    print(f"Game over! You've collected {floor(coins)} coins.")

print("Your path:")
for path in your_path:
    print(path)