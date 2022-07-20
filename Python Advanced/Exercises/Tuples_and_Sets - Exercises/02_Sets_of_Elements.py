n, m = [int(x) for x in input().split()]

first = set()
[first.add(int(input())) for _ in range(n)]

second = set()
[second.add(int(input())) for _ in range(m)]

result = first.intersection(second)
[print(num) for num in result]




# n, m = [int(x) for x in input().split()]
#
# first = set()
# second = set()
#
# for _ in range(n):
#     first.add(int(input()))
#
# for _ in range(m):
#     second.add(int(input()))
#
# result = first.intersection(second)
# for num in result:
#     print(num)







# n, m = [int(x) for x in input().split()]
#
# unique_nums_in_n = set()
# unique_nums_in_m = set()
#
# for _ in range(n):
#     num = int(input())
#     unique_nums_in_n.add(num)
#
# for _ in range(m):
#     num = int(input())
#     unique_nums_in_m.add(num)
#
# elements_repeated_in_both_sets = unique_nums_in_n.intersection(unique_nums_in_m)
# print("\n".join([str(el) for el in elements_repeated_in_both_sets]))
# # print("\n".join([str(el) for el in unique_el_in_n & unique_el_in_m]))