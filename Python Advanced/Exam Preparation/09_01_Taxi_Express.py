from collections import deque


customers = deque([int(x) for x in input().split(", ")])
taxis = deque([int(x) for x in input().split(", ")])
total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]

    if customer <= taxi:
        total_time += customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: ", end="")
    print(*customers, sep=", ")
else:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")



# from collections import deque
#
#
# customers = deque([int(x) for x in input().split(", ")])
# taxis = deque([int(x) for x in input().split(", ")])
# total_time = 0
#
# while customers and taxis:
#     customer = customers.popleft()
#     taxi = taxis.pop()
#
#     if customer <= taxi:
#         total_time += customer
#     else:
#         customers.appendleft(customer)
#
# if customers:
#     print("Not all customers were driven to their destinations")
#     print(f"Customers left: ", end="")
#     print(*customers, sep=", ")
# else:
#     print(f"All customers were driven to their destinations")
#     print(f"Total time: {total_time} minutes")