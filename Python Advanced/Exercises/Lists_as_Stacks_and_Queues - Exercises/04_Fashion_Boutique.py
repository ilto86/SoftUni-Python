# from collections import deque
#
# box_of_clothes = [int(x) for x in input().split()]
# clothes = deque(box_of_clothes)
# capacity_for_one_rack = int(input())
# count = 0
#
# while clothes:
#     capacity = capacity_for_one_rack
#     for i in range(capacity_for_one_rack):
#         each_clothes = clothes.pop()
#         if capacity - each_clothes < 0:
#             count += 1
#             clothes.append(each_clothes)
#             break
#         else:
#             capacity -= each_clothes
#             if not clothes:
#                 count += 1
#                 break
#
# print(count)








# clothes = [int(x) for x in input().split()]
# rack_capacity = int(input())
#
# used_racks = 1
# current_rack = rack_capacity
#
# while clothes:
#     current_piece = clothes[-1]
#
#     if current_piece <= current_rack:
#         clothes.pop()
#         current_rack -= current_piece
#     else:
#         used_racks += 1
#         current_rack = rack_capacity
#
# print(used_racks)








clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
racks_counter = 1

while clothes:
    piece_of_clothing = clothes[-1]
    if piece_of_clothing > current_rack_capacity:
        racks_counter += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= piece_of_clothing
        clothes.pop()

print(racks_counter)