def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_around_bombs(matrix, row, col):
    result = 0
    if is_inside(row, col - 1, size) and matrix[row][col - 1] == "*":
        result += 1
    if is_inside(row, col + 1, size) and matrix[row][col + 1] == "*":
        result += 1
    if is_inside(row - 1, col, size) and matrix[row - 1][col] == "*":
        result += 1
    if is_inside(row + 1, col, size) and matrix[row + 1][col] == "*":
        result += 1
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] == "*":
        result += 1
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] == "*":
        result += 1
    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] == "*":
        result += 1
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] == "*":
        result += 1

    return result


size = int(input())
numbers_bombs = int(input())
mines_field = []

for _ in range(size):
    mines_field.append([0]* size)

for i in range(numbers_bombs):
    row_position, col_position = [int(x) for x in input()[1:-1].split(', ')] # make string "(0, 3)" in int number row = 0, col = 3
    mines_field[row_position][col_position] = "*"

for row in range(size):
    for col in range(size):
        if mines_field[row][col] == "*":
            continue
        mines_field[row][col] = get_around_bombs(mines_field, row, col)

for row in mines_field:
    print(*row, sep=" ")
