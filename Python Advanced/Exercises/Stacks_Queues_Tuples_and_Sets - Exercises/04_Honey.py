from collections import deque

bees = deque([int(x) for x in input().split()])
nectar_list = [int(x) for x in input().split()]
operators = deque(input().split())

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

honey = 0

while bees and nectar_list:
    bee = bees.popleft()
    nectar = nectar_list.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = operators.popleft()
    honey += abs(operations[operator](bee, nectar))

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar_list:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_list])}")






# from collections import deque
#
# bees = deque([x for x in input().split()])
# nectar_list = [x for x in input().split()]
# symbols = deque(input().split())
# total_honey = 0
#
# while bees and nectar_list:
#     bee = int(bees[0])
#     nectar = int(nectar_list[-1])
#
#     if bee > nectar:
#         nectar_list.pop()
#     else:
#         operator = symbols[0]
#         if operator == "+":
#             total_honey += abs(bee + nectar)
#         elif operator == "-":
#             total_honey += abs(bee - nectar)
#         elif operator == "*":
#             total_honey += abs(bee * nectar)
#         elif operator == "/" and nectar > 0:
#             total_honey += abs(bee / nectar)
#         bees.popleft()
#         nectar_list.pop()
#         symbols.popleft()
#
# print(f"Total honey made: {total_honey}")
#
# if bees:
#     print(f"Bees left: {', '.join(bees)}")
#
# if nectar_list:
#     print(f"Nectar left: {', '.join(nectar_list)}")