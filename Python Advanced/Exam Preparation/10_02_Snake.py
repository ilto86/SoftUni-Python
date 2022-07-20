def get_next_pos(row, col, direction):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


def is_outside(row, col, size):
    return 0 > row or row >= size or 0 > col or col >= size


territory_size = int(input())

territory = []
snake_row = 0
snake_col = 0
first_burrow = tuple()
second_burrow = tuple()
food = 0
game_over = False

for row in range(territory_size):
    row_elements = list(input())
    for col in range(territory_size):
        if row_elements[col] == "S":
            snake_row = row
            snake_col = col
        if row_elements[col] == "B":
            if not first_burrow:
                first_burrow = (row, col)
            else:
                second_burrow = (row, col)
    territory.append(row_elements)



while food < 10:
    territory[snake_row][snake_col] = "."
    direction = input()
    next_row, next_col = get_next_pos(snake_row, snake_col, direction)

    if is_outside(next_row, next_col, territory_size):
        game_over = True
        break

    if territory[next_row][next_col] == "*":
        food += 1
        territory[next_row][next_col] = "S"

    if territory[next_row][next_col] == "B":
        territory[next_row][next_col] = "."
        first_row, first_col = first_burrow
        second_row, second_col = second_burrow
        if (next_row, next_col) == (first_row, first_col):
            next_row, next_col = second_row, second_col
            territory[next_row][next_col] = "S"
        else:
            next_row, next_col = first_row, first_col
            territory[next_row][next_col] = "S"

    snake_row, snake_col = next_row, next_col

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")
for row in territory:
    print(*row, sep="")