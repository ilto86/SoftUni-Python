# single_str = input().split(", ")
# single_int = [int(nums) for nums in single_str]
# zeros = []
#
# for n in single_str:
#     if 0 in single_int:
#         single_int.remove(0)
#         zeros.append(0)
#
#
# for i in zeros:
#     single_int.append(i)
#
#
# print(single_int)

num_list = [int(num) for num in input().split(', ')]

for idx in range(len(num_list)-1, -1, -1):
    if num_list[idx] == 0:
        zero = num_list.pop(idx)
        num_list.append(zero)

print(num_list)