# def get_sum_of_the_column(board, row, col, size):
#     result = 0
#     current_row = row
#     for up in range(size):
#         if is_inside(current_row - 1, col, size):
#             result += board[current_row - 1][col]
#             current_row -= 1
#         else:
#             break
#     next_row = row
#     for down in range(size):
#         if is_inside(next_row + 1, col, size):
#             result += board[next_row + 1][col]
#             next_row += 1
#         else:
#             break
#
#     return result
#
#
# def is_inside(r, c, n):
#     if 0 <= r < n and 0 <= c < n:
#         return True
#
#
# board_size = 6
# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for x in range(board_size)]
# points = 0
#
# for throw in range(3):
#     coordinates = [int(x) for x in input()[1:-1].split(', ')]
#     throw_row, throw_col = coordinates
#
#     if 0 <= throw_row < board_size and 0 <= throw_col < board_size:
#         if matrix[throw_row][throw_col] == "B":
#             matrix[throw_row][throw_col] = 0
#             points += get_sum_of_the_column(matrix, throw_row, throw_col, board_size)
#
# if points < 100:
#     neeed_points_for_prize = 100 - points
#     print(f"Sorry! You need {neeed_points_for_prize} points more to win a prize.")
# elif 100 <= points <= 199:
#     print(f"Good job! You scored {points} points, and you've won Football.")
# elif 200 <= points <= 299:
#     print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
# else:
#     print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")





size_of_matrix = 6
matrix = []
bucket_position = {}
points = 0

for row in range(size_of_matrix):
    row_element = [int(x) if x.isdigit() else x for x in input().split()]
    for col in range(size_of_matrix):
        if row_element[col] == 'B':
            bucket_position[(row, col)] = 0
    matrix.append(row_element)

for k, v in bucket_position.items():
    r, c = k
    result = 0
    for idx_row, row in enumerate(matrix):
        for idx_col, col in enumerate(row):
            if idx_row != r and idx_col == c:
                result += col
    bucket_position[k] = result

for commands in range(3):
    throw_row, throw_col = [int(x) for x in input()[1:-1].split(', ')]

    if 0 <= throw_row < size_of_matrix and 0 <= throw_col < size_of_matrix:
        if (throw_row, throw_col) in bucket_position:
            points += bucket_position[(throw_row, throw_col)]
            del bucket_position[(throw_row, throw_col)]

if points < 100:
    needed_points = 100 - points
    print(f"Sorry! You need {needed_points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")