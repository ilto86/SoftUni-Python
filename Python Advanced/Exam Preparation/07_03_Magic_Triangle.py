def get_magic_triangle(n):
    triangle = []
    for i in range(1, n + 1):
        first_num = 1
        number_to_append = []
        for j in range(1, i + 1):
            number_to_append.append(first_num)
            first_num = first_num * (i - j) // j

        triangle.append(number_to_append)

    return triangle


print(get_magic_triangle(5))


# triangle = []
# for i in range(1, 5 + 1):
#     first_num = 1
#     number_to_append = []
#     for j in range(1, i + 1):
#         number_to_append.append(first_num)
#         first_num = first_num * (i - j) // j
#
#     triangle.append(number_to_append)
#
# for row in triangle:
#     print(*row, sep=", ")











# def get_magic_triangle(count):
# 	magic_triangle = []
#
# 	for i in range(count):
# 		magic_triangle.append([1] * (i + 1))
#
# 	for i in range(2, count):
# 		for j in range(1, i):
# 			magic_triangle[i][j] = magic_triangle[i - 1][j - 1] + magic_triangle[i - 1][j]
#
# 	return magic_triangle
#
# print(get_magic_triangle(5))




# def pascal_triangle(num_rows):
#     '''Print Pascal's triangle with num_rows.'''
#     if num_rows == 1:
#         return [[1]] # base case is reached!
#     else:
#         result = pascal_triangle(num_rows - 1) # recursive call to pascal_triangle
#         # use previous row to calculate current row
#         current_row = [1] # every row starts with 1
#         previous_row = result[-1]
#         for i in range(len(previous_row)-1):
#             # sum of 2 entries directly above
#             current_row.append(previous_row[i] + previous_row[i+1])
#         current_row += [1] # every row ends with 1
#         result.append(current_row)
#         return result
#
# print(pascal_triangle(5))




# def get_magic_triangle(n):
# 	magic_triangle = []
# 	i = [1]
# 	j = [0]
#
# 	for x in range(max(n,0)):
# 		magic_triangle.append(i)
# 		i = [left + right for left, right in zip(i+j, j+i)]
#
# 	return magic_triangle
#
#
# print(get_magic_triangle(5))