from collections import deque

chocolate_packages = [int(x) for x in input().split(',')]
milk_cups = deque([int(x) for x in input().split(',')])

milkshakes = 0

while chocolate_packages and milk_cups and milkshakes < 5:
    chocolate = chocolate_packages.pop()
    milk = milk_cups.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    if milk <= 0:
        chocolate_packages.append(chocolate)
        continue
    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolate_packages.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate_packages:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate_packages])}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")






# from collections import deque
#
# chocolates = deque([int(x) for x in input().split(", ")])
# cups_of_milk = deque([int(x) for x in input().split(", ")])
# count = 0
#
# while chocolates and cups_of_milk and count < 5:
#     choco = chocolates[-1]
#     milk = cups_of_milk[0]
#
#     if choco < 1 and milk < 1:
#         chocolates.pop()
#         cups_of_milk.popleft()
#         continue
#     if choco < 1:
#         chocolates.pop()
#         continue
#     if milk < 1:
#         cups_of_milk.popleft()
#         continue
#
#     if choco == milk:
#         chocolates.pop()
#         cups_of_milk.popleft()
#         count += 1
#     else:
#         cups_of_milk.append(cups_of_milk.popleft())
#         chocolates.append(chocolates.pop() - 5)
#
# if count > 4:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
# if chocolates:
#     print(f"Chocolate: {', '.join(map(str, chocolates))}")
# else:
#     print("Chocolate: empty")
# if cups_of_milk:
#     print(f"Milk: {', '.join(map(str, cups_of_milk))}")
# else:
#     print("Milk: empty")