# rows = int(input())
# matrix = []
#
# for i in range(rows):
#     row = input().split(", ")
#     matrix.append(list(map(int, row)))
#
# evens = [[x for x in row if x % 2 == 0] for row in matrix]
# print(evens)

# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     nums = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
#     matrix.append(nums)
# print(matrix)





# rows = int(input())
#
# matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(rows)]
#
# print(matrix)




# print([[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(int(input()))])




# n = int(input())
#
# result = []
#
# for _ in range(n):
#     row = [int(x) for x in input().split(", ")]
#     result.append([x for x in row if x % 2 == 0])
#
# print(result)

n = int(input())
matrix = [[int(x) for x in input().split(", ")]for _ in range(n)]
print([x for x in row if x % 2 == 0]for row in matrix)