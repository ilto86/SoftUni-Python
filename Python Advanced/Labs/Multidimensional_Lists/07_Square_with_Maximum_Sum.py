# rows, cols = [int(el) for el in input().split(", ")]
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(el) for el in input().split(", ")])
#
# max_sum = -999999999999999
# max_sum_matrix = []
#
# for row_index in range(rows - 1):
#     for col_index in range(cols -1):
#         sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index+1],
#                       matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]
#
#         current_sum = sum(sub_matrix)
#         if current_sum > max_sum:  # Show the firs max_sum_matrix and max_sum, when if current_sum >= max_sum: show the last one
#             max_sum = current_sum
#             max_sum_matrix = sub_matrix.copy()
#
# print(max_sum_matrix[0], max_sum_matrix[1])
# print(max_sum_matrix[2], max_sum_matrix[3])
# print(max_sum)






rows, cols = [int(el) for el in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
max_result = 0
max_combination = []

for row in range(rows -1):
    for col in range(cols - 1):
        result = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if result > max_result:
            max_result = result
            max_combination.append([matrix[row][col], matrix[row][col + 1]])
            max_combination.append([matrix[row + 1][col], matrix[row + 1][col + 1]])

print(*max_combination[-2])
print(*max_combination[-1])
print(max_result)