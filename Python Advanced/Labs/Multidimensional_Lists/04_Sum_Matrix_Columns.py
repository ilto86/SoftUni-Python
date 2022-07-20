# rows_count, columns_count = [int(el) for el in input().split(", ")]
# matrix = []
#
# for _ in range(rows_count):
#     row = [int(el) for el in input().split()]
#     matrix.append(row)
#
# result = []
#
# for column_index in range(columns_count):
#     column_sum = 0
#     for row_index in range(rows_count):
#         column_sum += matrix[row_index][column_index]
#     result.append(column_sum)
#
# [print(x) for x in result]







# rows_count, columns_count = [int(el) for el in input().split(", ")]
# matrix = []
#
# for _ in range(rows_count):
#     nums = [int(el) for el in input().split()]
#     matrix.append(nums)
#
# for col_index in range(columns_count):
#     result = 0
#     for row_index in range(rows_count):
#         result += matrix[row_index][col_index]
#     print(result)








# rows, cols = [int(el) for el in input().split(", ")]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# for col_index in range(cols):
#     result = 0
#     for row_index in range(rows):
#         result += matrix[row_index][col_index]
#     print(result)


# input
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0

# output
# 12
# 10
# 19
# 20
# 8
# 7


import sys
from io import StringIO

test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 6 6
4 6 7 9 1 0'''

test_input2 = '''3, 3
1 2 3
4 5 6
7 8 9'''

sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

def get_column_sums(matrix):
    column_sums = [0] * columns_count

    for row_index in range(rows_count):
        for column_index in range(columns_count):
            column_sums[-1] += matrix[row_index][column_index]

            return column_sums

rows_count, columns_count = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split()])

column_sums = [0] * columns_count

for row_index in range(rows_count):
    for column_index in range(columns_count):
        column_sums[column_index] += matrix[row_index][column_index]

[print(x) for x in columns_count]