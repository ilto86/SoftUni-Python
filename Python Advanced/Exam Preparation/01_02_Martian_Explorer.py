from collections import deque


def get_moves(command, row, col):
    if command == "up":
        return row - 1, col
    if command == "down":
        return row + 1, col
    if command == "left":
        return row, col - 1
    if command == "right":
        return row, col + 1


def is_outside(row, col, size):
    if 0 > row:
        return (size - 1, col)
    if row >= size:
        return  (0, col)
    if 0 > col:
        return (row, size - 1)
    if col >= size:
        return  (row, 0)


SIZE = 6

matrix = []
rover_row = 0
rover_col = 0
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

for row in range(SIZE):
    row_elements = input().split()
    for col in range(SIZE):
        if row_elements[col] == "E":
            rover_row, rover_col = row, col
    matrix.append(row_elements)

action = deque(input().split(", "))
while action:
    direction = action.popleft()
    next_row, next_col = get_moves(direction, rover_row, rover_col)

    if 0 > next_row or next_row >= SIZE or 0 > next_col or next_col >= SIZE:
        next_row, next_col = is_outside(next_row, next_col, SIZE)

    if matrix[next_row][next_col] == "W":
        water_deposit += 1
        matrix[next_row][next_col] = "-"
        print(f"Water deposit found at {next_row, next_col}")

    if matrix[next_row][next_col] == "M":
        metal_deposit += 1
        matrix[next_row][next_col] = "-"
        print(f"Metal deposit found at {next_row, next_col}")

    if matrix[next_row][next_col] == "C":
        concrete_deposit += 1
        matrix[next_row][next_col] = "-"
        print(f"Concrete deposit found at {next_row, next_col}")

    if matrix[next_row][next_col] == "R":
        print(f"Rover got broken at {next_row, next_col}")
        break

    rover_row, rover_col = next_row, next_col

if water_deposit and metal_deposit and concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")