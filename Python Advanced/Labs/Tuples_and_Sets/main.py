#    ----------------------TUPLES-----------------------------------------------



# # tt = (1, 2, 3, 4, 5)
#
# tt = (
#     [1, 2, 3],
#     {},
#     (4, 5, 6),
# )
#
# print(tt)
#
# # tt[0] = 5
# tt[0].append(-4)
# tt[1]["doncho"] = "Minkov"
# print(tt)

# a = 1,
#
# print(type(a))
# print(a)

# a = [5, 6, -15]
# b = (10, 2, 3)
#
# print(type(a))
# print(type(b))
#
# print(a[0])
# print(b[0])
#
# print(a.index(5))
# print(b.index(10))



# a = [5, 6, -15, 5]
# b = (10, 2, 3, 10)
#
# names = {"Test": 5}
#
# c = (names)
# d = (names, )
# print(a.count(5))
# print(b.count(10))
# print(type(c))
# print(c)
# print(type(d))
# print(d)
#
# names.update({"Test2": 100})
# print(c)
# print(d)


# def sum_nums(b,a):
#     return b + a, "completed"
#
# res = sum_nums(95, 4)
# print(res)
# print(type(res))



# nums = (1, 2, 3)
#
# print(*nums)
# print(" ".join([str(el) for el in nums]))
# print(*nums, sep=",")
# print(",".join([str(el) for el in nums]))
# print(*nums, sep="<->")
# print("<->".join([str(el) for el in nums]))


# def sum_nums(args=None):
#     if args is None:
#         args = [1, 2, 3]
#     return sum(args)
# print(sum_nums())


# def sum_nums(args=(1, 2, 3)):
#     return sum(args)
# print(sum_nums())


# t = 1, 2, 3
# print(t)

# data = (1, 2, 3)
# x, y, z = data
# print(x)
# print(y)
# print(z)

# numbers = (1, 2, 1, 3, 1)
# print(numbers.count(1)) # show how many times number 1 is in tuple
# print(numbers[1]) # show what is in first index



# nums = (float(el) for el in input().split())
#
# occurences = {}
#
# for num in nums:
#     if num not in occurences:
#         occurences[num] = 0
#     occurences[num] += 1
#
# print(list(occurences.items()))

# for kvp in occurences.items():
#     print(f"{kvp[0]} - {kvp[1]} times")
#     print(type(kvp))
#
# for key,value in occurences.items():
#     print(f"{key} - {value} times")



# nums = tuple(float(el) for el in input().split())
#
# occurences = {}
#
# for num in nums:
#     occurences[num] = nums.count(num)
#
# for kvp in occurences.items():  # for key,value in occurences.items():
#     print(f"{kvp[0]} - {kvp[1]} times") #     print(f"{key} - {value} times")




#   ---------------------------SETS-----------------------------------------------


# a = set([1, 2, 3, 4])
# b = set([3, 4, 5, 6])
#
# print(a | b)  # print(a.union(b))
# print(a.union(b))  # print(a | b)
# print(a & b)  # print(a.intersection(b))
# print(a.intersection(b))  # print(a & b)
# print(a <= b)  # print(a.issubset(b))
# print(a.issubset(b))  # print(a <= b)
# print(a >= b)  # print(a.issuperset(b))
# print(a.issuperset(b))  # print(a >= b)
# print(a - b)  # print(a.difference(b))
# print(a.difference(b))  # print(a - b)
# print(a ^ b)  # print(a.symmetric_difference(b))
# print(a.symmetric_difference(b))  # print(a ^ b)





# nums = [1, 2, 3, 4, 4, 5, 6, 2, 1]
# unique = {num for num in nums}
#
# print(unique)  # unique is Set Comprehension


# nums = ["aa", 1, 3, 1, 2, "a", 4, 5, 1, -15]
# print(set(nums))
#
# nums = {"aa", 1, 3, 1, 2, "a", 4, 5, 1, -15}
# print(type(nums))


'''
Sets:

- Search, add, remove is very, very, very fast
- Contains only unique values
    -*unique values

- Unordered (with hash tables)
- Ordered (with tree)

'''


# ss = set([1, 2, 3, 4, 5] + list(range(6, 67)))
#
# [ss.add(6) for _ in range(5)]
# print(ss)
#
# ss.remove(6)
# ss.add(4)
#
# print(4 in ss)
# print(6 in ss)




# import time

# ll = list(range(1024*32))
# ss = set(ll)
#
# result = False
# start = time.time()
# for v in ss:
#     result = v in ss
# end = time.time()
# print(f"Set: {end - start} s")
#
#
# result = False
# start = time.time()
# for v in ll:
#     result = v in ll
# end = time.time()
# print(f"List: {end - start} s")





# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = {1, 2, 3, 4, 5}
#
# print(f"s1 = {s1}")
# print(f"s2 = {s2}")
# print(f"s3 = {s3}")
# print(f"{s1} | {s2} = {s1 | s2}")
# print(f"{s1} union {s2} = {s1.union(s2)}")
# print(f"{s1} & {s2} = {s1 & s2}")
# print(f"{s1} intersection {s2} = {s1.intersection(s2)}")
#
# print(f"{s2}.issubset({3}) = {s3.issubset(s1)}")


# -------------------- Sets Comprehension --------------------

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
#
# print([x % 3 for x in ll])
# print()


# ll = [1, 7, 6, -1, 10, 8, -2, 12, 4 , -7, 5, 2, 13, 3, 9, 14, 11]
# target = 8
# targets = set()
#
# for value in ll:
#     if value in targets:
#         print("Found")
#         print(value)
#     else:
#         targets.add(target - value)
#         print(targets)

# ll = [int(x) for x in input().split()]
# target = int(input())
# targets = set()
# values_map = {}
#
# for value in ll:
#     if value in targets:
#         p1 = value
#         p2 = values_map[value]
#         print(f"{p1} + {p2} = {target}")
#     else:
#         targets.add(target - value)
#         values_map[target - value] = value







# from itertools import combinations
#
# seq = [1, 5, 4, 2, 2, 3, 1, 3, 2]    #   [int(x) for x in input().split()]
# target = 4                           #  int(input())
# iterations = 0
# pairs_set = set()
#
# for first, second in combinations(seq, 2):
#     iterations += 1
#     if first + second == target:
#         print(f"{first} + {second} = {target}")
#         pairs_set.add(f"{first}, {second}")
#
# print(f"Iterations done: {iterations}")
# for pair in pairs_set:
#     print(f"({pair})")

