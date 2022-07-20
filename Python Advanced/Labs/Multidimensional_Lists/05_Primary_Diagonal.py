# n = int(input())
# matrix = []
#
# for _ in range(n):
#     nums = [int(el) for el in input().split()]
#     matrix.append(nums)
#
# diagonal_sum = 0
# for row_index in range(n):
#     for col_index in range(n):
#         if row_index == col_index:
#             diagonal_sum += matrix[row_index][col_index]
#
# print(diagonal_sum)




# n = int(input())
# matrix = []
#
# for _ in range(n):
#     nums = [int(el) for el in input().split()]
#     matrix.append(nums)
#
# diagonal = 0
# for index in range(n):
#     diagonal += matrix[index][index]
#
# print(diagonal)



# rows = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# result = 0
#
# for row_index in range(rows):
#     result += matrix[row_index][row_index]
#
# print(result)




import sys
from io import StringIO

test_input1 = '''3
11 2 4 
4 5 6
10 8 -12
'''

test_input2 = '''3
1 2 3
4 5 6
7 8 9
'''

# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)


def get_primary_diagonal(matrix):
    n = len(matrix)
    # the_sum = 0
    # for i in range(n):
    #     the_sum += matrix[i][i]
    #     return the_sum
    return sum(matrix[i][i] for i in range(n))

def get_secondary_diagonal(matrix):
    n = len(matrix)
    return sum(matrix[i][n - i -1] for i in range(n))

n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

print(get_primary_diagonal(matrix))
print(get_secondary_diagonal(matrix))
