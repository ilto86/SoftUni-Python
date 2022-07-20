# from collections import deque
#
# quantity_of_the_food = int(input())
# quantity_of_food_in_each_order = [int(x) for x in input().split()]
#
# orders_in_a_queue = deque(quantity_of_food_in_each_order)
#
# print(max(orders_in_a_queue))
#
# while orders_in_a_queue:
#     each_order = orders_in_a_queue.popleft()
#     if quantity_of_the_food - each_order < 0:
#         orders_in_a_queue.appendleft(each_order)
#         break
#     else:
#         quantity_of_the_food -= each_order
#
# if orders_in_a_queue:
#     print(f"Orders left: {' '.join(map(str, orders_in_a_queue))}")
# else:
#     print("Orders complete")





from collections import deque

total_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]

    if current_order > total_food:
        break

    total_food -= current_order
    orders.popleft()

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
    # print(f"Orders left:",*orders)
else:
    print("Orders complete")