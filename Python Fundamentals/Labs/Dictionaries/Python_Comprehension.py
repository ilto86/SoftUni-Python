nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([x % 3 for x in nums])
print({x % 3 for x in nums})
print({x: x % 3 for x in nums})


print({x: nums.count(x) for x in nums})   # this is same

result = {}
# for x in nums:                          # this is same
#     result[x] = 0
#     for y in nums:
#         if x == y:
#             result[x] += 1
# print(result)

for x in nums:                            # this is same
    if x not in result:
        result[x] = 0
    result[x] += 1
print(result)