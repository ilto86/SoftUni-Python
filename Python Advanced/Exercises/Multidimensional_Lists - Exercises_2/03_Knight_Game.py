# def find_count(board, row, col):
#     moves = [
#         [row - 2, col - 1],
#         [row - 2, col + 1],
#         [row - 1, col - 2],
#         [row - 1, col + 2],
#         [row + 1, col - 2],
#         [row + 1, col + 2],
#         [row + 2, col - 1],
#         [row + 2, col + 1],
#     ]
#     result = 0
#     for r, c in moves:
#         if 0 <= r < len(board) and 0 <= c < len(board) and  board[r][c] == "K":
#             result += 1
#     return result
#
# size = int(input())
#
# board = []
# removed_knights_counter = 0
#
# for _ in range(size):
#     board.append(list(input()))
#
# while True:
#     best_count = 0
#     knight_row = 0
#     knight_col = 0
#     for row in range(size):
#         for col in range(size):
#             if board[row][col] == "0":
#                 continue
#             count = find_count(board, row, col)
#             if count > best_count:
#                 best_count = count
#                 knight_row = row
#                 knight_col = col
#
#     if best_count == 0:
#         break
#     board[knight_row][knight_col] = "0"
#     removed_knights_counter += 1
#
# print(removed_knights_counter)






def get_knights_move(matrix, row, col):
    moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
        ]
    result = 0
    for r, c in moves:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and  matrix[r][c] == "K":
            result += 1
    return result



rows_cols = int(input())
matrix = []
removed_knights = 0

for _ in range(rows_cols):
    matrix.append(list(input()))

while True:
    best_sum = 0
    knight_row = 0
    knight_col = 0
    for row in range(rows_cols):
        for col in range(rows_cols):
            if matrix[row][col] == "0":
                continue
            count = get_knights_move(matrix, row, col)
            if count > best_sum:
                best_sum = count
                knight_row = row
                knight_col = col

    if best_sum == 0:
        break
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)
