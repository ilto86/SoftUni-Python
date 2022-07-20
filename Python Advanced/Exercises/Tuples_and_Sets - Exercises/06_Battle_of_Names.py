n = int(input())

even = set()
odd = set()

for row in range(1, n + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row
    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    result = odd.union(even)
elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)

print(*result, sep=", ")














# n = int(input())
# odd_set = set()
# even_set = set()
#
# for i in range(1, n + 1):
#     name = input()
#     ascii_value = 0
#     for ch in name:
#         ascii_value += ord(ch)
#     sum = int(ascii_value / i)
#     if sum % 2 == 0:
#         even_set.add(sum)
#     else:
#         odd_set.add(sum)
# sum_odd = 0
# sum_even = 0
# for num in odd_set:
#     sum_odd += num
# for num in even_set:
#     sum_even += num
#
# if sum_even > sum_odd:
#     print(*odd_set)
#     print(*even_set)
# else:
#     print(even_set)
#     print(odd_set)