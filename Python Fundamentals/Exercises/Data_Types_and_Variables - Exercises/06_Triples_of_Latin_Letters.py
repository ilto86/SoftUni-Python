# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             print(f"{chr(i + 97)}{chr(j + 97)}{chr(k + 97)}")

n = int(input())

result_i = ""
result_j = ""
result_k = ""

for i in range(n):
    result_i = chr(i + 97)
    for j in range(n):
        result_j = chr(j + 97)
        for k in range(n):
            result_k = chr(k + 97)
            print(f"{result_i}{result_j}{result_k}")