# def read_matrix():
#     n, m = [int(x) for x in input().split(", ")]
#     matrix = []
#
#     for _ in range(n):
#         row = [int(x) for x in input().split(", ")]
#         matrix.append(row)
#
#         return read_matrix

# matrix = read_matrix()


n, m = [int(x) for x in input().split(", ")]
matrix = []
matrix_sum = 0

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    matrix_sum += sum(row)

print(matrix_sum)
print(matrix)










# rows, cols = [int(el) for el in input().split(", ")]
# matrix = []
# result = 0
#
# for _ in range(rows):
#     nums = [int(el) for el in input().split(", ")]
#     result += sum(nums)
#     matrix.append(nums)
#
# print(result)
# print(matrix)





# rows, cols = [int(el) for el in input().split(", ")]
# matrix = []
#
#
# for _ in range(rows):
#     nums = [int(el) for el in input().split(", ")]
#     matrix.append(nums)
#
# result = 0
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         result += matrix[row_index][col_index]
#
# print(result)
# print(matrix)
