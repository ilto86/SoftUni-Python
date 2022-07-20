# expression = input()
#
# per_stack = []
#
# for index in range(len(expression)):
#         if expression[index] == "(":
#             per_stack.append(index)
#         elif expression[index] == ")":
#             start_index = per_stack.pop()
#             print(expression[start_index:index+1])







# text = input()
# index = []
#
# for i in range(len(text)):
#     if text[i] == "(":
#         index.append(int(i))
#     elif text[i] == ")":
#         start_index = index.pop()
#         print(text[start_index:i+1])










expression = input()

open_brackets_indices = []

for index in range(len(expression)):
    if expression[index] == "(":
        open_brackets_indices.append(index)
    elif expression[index] == ")":
        last_open_brackets_index = open_brackets_indices.pop()
        closed_brackets_index = index + 1
        print(expression[last_open_brackets_index:closed_brackets_index])