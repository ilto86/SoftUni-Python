# n = int(input())
# matrix = []
#
# for _ in range(n):
#     matrix.append(list(input()))
#
# position = None   # position = []
# searched_char = input()
#
# for row_index in range(n):
#     for col_index in range(n):
#         if searched_char == matrix[row_index][col_index]:
#             position = (row_index, col_index)     # position = [row_index, col_index]
#             print(position)
#             break
#     if position:
#         break
#
# if not position:
#     print(f"{searched_char} does not occur in the matrix")




# n = int(input())
# matrix = [list(input()) for _ in range(n)]
# searched_char = input()
# positions = None
#
# for row in matrix:
#     if searched_char in row:
#         cordinates = (matrix.index(row), row.index(searched_char))
#         print(positions)
#         break
#
# if not positions:
#     print(f"{searched_char} does not occur in the matrix")






# Input
# 6
# ABCDEF
# GHIKLM
# NOPRST
# QUXYZ!
# 123456
# 987654
# 0

# Output
# (2, 1)


# rows = int(input())
# matrix = [[x for x in input()] for _ in range(rows)]
# searched_symbol = input()
# not_found = True
#
# for row in matrix:
#     if searched_symbol in row:
#         position = matrix.index(row), row.index(searched_symbol)
#         print(position)
#         not_found = False
#         break
#
# if not_found:
#     print(f"{searched_symbol} does not occur in the matrix")
from main import row_index, column_index


def find_symbol(matrix, symbol):
    # for row_index in range(n):
    #     for column_index in range(n):
    #         if matrix[row_index][column_index] == symbol:
    #             return row_index, column_index
    # return  None
    for row_index in range(n):
        if symbol in matrix[row_index]:
            column_index = matrix[row_index].index(symbol)
            return row_index, column_index

n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

result = find_symbol(matrix, symbol)
if result:
    row_index, column_index = result
    print(f"({row_index}, {column_index})")
else:
    print(f"{symbol} does not occur in the matrix")