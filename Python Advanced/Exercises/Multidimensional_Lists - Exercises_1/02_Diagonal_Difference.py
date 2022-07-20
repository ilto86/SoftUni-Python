# size = int(input())
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])
#
# primary = []
# secondary = []
#
# for idx in range(size):
#     primary.append(matrix[idx][idx])
#     secondary.append(matrix[idx][size - idx - 1])
#
# primary_sum = sum(primary)
# secondary_sum = sum(secondary)
#
# print(abs(primary_sum - secondary_sum))



size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

primary = []
secondary = []

for idx in range(size):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size - idx - 1])

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(abs(primary_sum - secondary_sum))




# size = int(input())
#
# matrix = []
# primary_diagonal = []
# secondary_diagonal = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])
#
# for idx in range(size):
#     primary_diagonal.append(matrix[idx][idx])
#     secondary_diagonal.append(matrix[idx][size -1 -idx])
#
# print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))