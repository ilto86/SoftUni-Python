'''
Sum of 2

With ordered values:
1 1 2 2 2 3 3 4 5
target = 4
p1 = 1
p2 = 5

Algorithm:
current_sum = p1 + p2
current_sum <> target
if current_sum == target:
    Great!
elif current_sum < target:
    move p1 right
else: current_sum > target
    move p2 left


Without ordered values:
1 5 4 2 2 3 1 3 2
target = 4

targets = [
algorithms:
check if current_value is in targets:
if it is, Great!
else:
add target-current_value to targets


#1
values = 1 5 4 2 2 3 1 3 2
targets = {
current_value = 1

#2
values =[1 5 4 2 2 3 1 3 2]
targets = {3
current_value = 5
'''

# import  time
# ll = list(range(1024 * 8))
# target = 8
# targets = set()
# values_map = {}
#
# start = time.time()
#
# for value in ll:
#     if value in targets:
#         p1 = value
#         p2 = values_map[value]
#         print(f"{p1} + {p2} = {target}")
#     else:
#         targets.add(target - value)
#         values_map[target - value] = value
#
# end = time.time()
# print(f"{end - start} s")



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

# numbers = list(map(int, input().split()))
# target = int(input())
# iterations = 0
# summation_pairs = set()
#
# for main_index in range(len(numbers)):
#     for secondary_index in range(main_index + 1, len(numbers)):
#         iterations += 1
#         if numbers[main_index] + numbers[secondary_index] == target:
#             current_summation_pair = (numbers[main_index], numbers[secondary_index])
#             print(f"{numbers[main_index]} + {numbers[secondary_index]} = {target}")
#             summation_pairs.add(current_summation_pair)
# print(f"Iterations done: {iterations}")
# for pair in summation_pairs:
#     print(pair)



# nums_list = [int(x) for x in input().split()]
# target = int(input())
# iterations = 0
# pairs_set = set()
#
# for idx_1 in range(len(nums_list)):
#     for idx_2 in range(idx_1 + 1, len(nums_list)):
#         iterations += 1
#         num_1 = nums_list[idx_1]
#         num_2 = nums_list[idx_2]
#
#         if num_1 + num_2 == target:
#             current_pair = (num_1, num_2)
#             pairs_set.add(current_pair)
#
#             print(f"{num_1} + {num_2} = {target}")
#
# print(f"Iterations done: {iterations}")
#
# for pair in pairs_set:
#     print(pair)



from itertools import combinations

seq = [int(x) for x in input().split()]
target = int(input())
iterations = 0
pairs_set = set()

for first, second in combinations(seq, 2):
    iterations += 1
    if first + second == target:
        print(f"{first} + {second} = {target}")
        pairs_set.add(f"{first}, {second}")

print(f"Iterations done: {iterations}")
for pair in pairs_set:
    print(f"({pair})")