from collections import deque

string_expression = [int(x) for x in input().split()]
queue_string = deque(string_expression)
list_num = list()
operators = ["+", "-", "*", "/"]
result = 0
idx = 0

while queue_string:
    num_1 = 0
    num_2 = 0

    if queue_string[idx] in operators:
        list_num.append(queue_string.popleft())
        num_1 = int(list_num[0])
        if queue_string[idx].isdigit():
            list_num.append(queue_string.popleft())
            list_num.append(queue_string.popleft())
            num_2 = int(list_num[1])
            el = list_num[2]
        if idx == 0:
            if el == "+":
                result = num_1 + num_2
            elif el == "-":
                result = num_1 - num_2
            elif el == "*":
                result = num_1 * num_2
            elif el == "/":
                result = int(num_1 / num_2)
    else:
        idx += 1
