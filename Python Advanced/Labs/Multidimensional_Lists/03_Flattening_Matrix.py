# rows_count = int(input())
# matrix = [map(int, input().split(', ')) for _ in range(rows_count)]
# flattened = [num for row in matrix for num in row]
# print(flattened)



# rows = int(input())
# result = []
#
# for _ in range(rows):
#     nums = [int(el) for el in input().split(", ")]
#     result += nums
# print(result)




# rows = int(input())
# result = []
#
# for _ in range(rows):
#     nums = [int(el) for el in input().split(", ")]
#     result.extend(nums)
# print(result)



# rows = int(input())
# matrix = []
#
# for _ in range(rows):
#     nums = [int(el) for el in input().split(", ")]
#     matrix.append(nums)
#
# result = []
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         result.append(matrix[row_index][col_index])
# print(result)








# row = int(input())
#
# matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]
#
# flattened = [num for row in matrix for num in row]
#
# print(matrix)
# print(flattened)




# rows = 2                     # rows = int(input())
#
# matrix = [                   # matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# flattened_matrix = []
#
# for row in matrix:           # flattened = [num for row in matrix for num in row]
#     for num in row:
#         flattened_matrix.append(num)
#
# print(flattened_matrix)




# rows = int(input())
# matrix = []
#
# for _ in range(rows):
#     line = input().split(", ")
#     matrix.append(line)
#
# flattened_matrix = []
#
# for row in matrix:
#     for num in row:
#         flattened_matrix.append(int(num))
#
# print(matrix)
# print(flattened_matrix)



# rows = int(input())
# flattened_matrix = []
#
# for _ in range(rows):
#     line = input().split(", ")
#     for el in line:
#         flattened_matrix.append(int(el))
#
# print(flattened_matrix)

