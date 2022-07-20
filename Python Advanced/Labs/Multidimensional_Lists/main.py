# rows, cols = [3, 3]
# matrix = [
#     ["1", "2", "3"],
#     ["4", "5", "6"],
#     ["7", "8", "9"]
#           ]
#
# for row in range(rows - 1):
#     for col in range(cols - 1):
#
#         if matrix[row][col] == "5":
#
#             print(matrix[row - 1][col - 1])  # 1 ↖
#             print(matrix[row - 1][col])  # 2 ↑
#             print(matrix[row - 1][col + 1])  # 3 ↗
#             print(matrix[row][col - 1])  # 4 ←
#             print(matrix[row][col])  # 5 ⑤ ⒌ ⑸ ⚒ ☕ ↻ 🔃
#             print(matrix[row][col + 1])  # 6 →
#             print(matrix[row + 1][col - 1])  # 7 ↙
#             print(matrix[row + 1][col])  # 8 ↓
#             print(matrix[row + 1][col + 1])  # 9 ↘







# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         matrix[i][j] += 1
# print(matrix)




# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")



# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [print(num) for num in [j for j in matrix]]




# n = int(input())
# matrix = []
#
# for _ in range(n):
#     data = input().split()
#     matrix.append(data)
# for row_index in range(len(matrix)):
#     print(*matrix[row_index])






# matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
#
# for row_index in range(len(matrix)):
#     print(*matrix[row_index])
#
# for _ in range(9):
#     row, col = [int(el) for el in input().split(", ")]
#     sign = input()
#     matrix[row][col] = sign
#     for row_index in range(len(matrix)):
#         print(*matrix[row_index])





# matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         print(matrix[row_index][col_index], end=" ")
#     print()
# for row_index in range(len(matrix)):
#     print(*matrix[row_index])






# matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         print(matrix[row_index][col_index], end="")
#     print()
#
# for _ in range(9):
#     sign = input()
#     row = int(input())
#     col = int(input())
#     matrix[row][col] = sign
#     for row_index in range(len(matrix)):
#         for col_index in range(len(matrix[row_index])):
#             print(matrix[row_index][col_index], end="")
#         print()



ll = [1, 2, 3, 4, 5, 6, 7]

ll2 = []

for v in ll:
    ll2.append(v + 1)

print(ll)
print(ll2)


ll3 = [v +1 for v in ll]
print(ll3)



mm = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print(mm)
print([v + 1 for row in mm for v in row])
print([[v + 1 for row in mm] for row in mm])

print([v + 1 for row in mm for v in row])




# ll = [
#     [1, 2, 3, 4],
#     [2, 3, 4, 5],
#     [3, 4, 5, 6],
#     [10, 11, 12]
# ]
#
# def is_even(number):
#     return number % 2 == 0
# def get_even(ll):
#     return [x for x in ll if is_even(x)]
#
# print([get_even(row) for row in ll])
#
#
# def is_even(number):
#     return number % 2 == 0
# def get_even(ll):
#     return [x for x in ll if is_even(x)]


# ll = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
# mm = [
#     [1, 2, 3, 4, 5]
#     [6, 7, 8, 9, 10]
#     [11, 12, 13, 14, 15]
# ]
# print(ll[4])
# print(mm[1])
# print(mm[1][3])


mm = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
n = len(mm)
m = len (mm[0])
for row_index in range(n):
    print(mm[row_index])
    for column_index in range(m):
        print(mm[row_index][column_index], end="")
    print()
