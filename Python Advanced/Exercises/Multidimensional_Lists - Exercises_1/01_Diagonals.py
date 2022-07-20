# size = int(input())
#
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split(', ')])
#
# primary = []
# secondary = []
#
# for idx in range(size):
#     primary.append(matrix[idx][idx])
#     secondary.append(matrix[idx][size - 1 - idx])
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")





size = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(size)]

primary = []
secondary = []

for idx in range(size):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size - 1 - idx])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")






# size = int(input())
#
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split(", ")])
#
# primary_diagonal = []
# secondary_diagonal = []
# for idx in range(size):
#
#     primary_diagonal.append(matrix[idx][idx])
#     secondary_diagonal.append(matrix[idx][size -1 -idx])
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")







# size = int(input())
#
# primary_diagonal = []
# secondary_diagonal = []
#
# for idx in range(size):
#     row_elements = [int(x) for x in input().split(", ")]
#     primary_diagonal.append(row_elements[idx])
#     secondary_diagonal.append(row_elements[size -1 -idx])
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")