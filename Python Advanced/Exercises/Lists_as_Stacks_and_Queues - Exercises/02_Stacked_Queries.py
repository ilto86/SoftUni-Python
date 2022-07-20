# n = int(input())
# stack = []
#
# for _ in range(n):
#     line_parts = input().split()
#     command = line_parts[0]
#
#     if command == "1":
#         number = int(line_parts[1])
#         stack.append(number)
#
#     elif command == "2" and stack:
#         stack.pop()
#
#     elif command == "3" and stack:
#         print(max(stack))
#
#     elif command == "4" and stack:
#         print(min(stack))
#
# while stack:
#     element = stack.pop()
#     if stack:
#         print(element, end=", ")
#     else:
#         print(element)






# count = int(input())
# queries = list()
#
# for _ in range(count):
#     number = input()
#     if len(number) > 1:
#         _, num = number.split()
#         queries.append(int(num))
#     elif number == "2" and queries:
#         queries.pop()
#     elif number == "3" and queries:
#         print(f"{max(queries)}")
#     elif number == "4" and queries:
#         print(f"{min(queries)}")
#
# queries = [str(x) for x in queries[::-1]]
# print(f'{", ".join(queries)}')





# count = int(input())
# queries = list()
#
# for i in range(1, count + 1):
#
#     number = [int(x) for x in input().split()]
#
#     if number[0] == 1:
#         num = number[1]
#         queries.append(num)
#
#     elif number[0] == 2:
#         if queries:
#             queries.pop()
#
#     elif number[0] == 3:
#         if queries:
#             print(f"{max(queries)}")
#
#     elif number[0] == 4:
#         if queries:
#             print(f"{min(queries)}")
#
# print(f"{', '.join(map(str, reversed(queries)))}")






stack = []
queries_count = int(input())

for _ in range(queries_count):
    query_parts = [int(x) for x in input().split()]
    command = query_parts[0]

    if command == 1:
        number = query_parts[1]
        stack.append(number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))