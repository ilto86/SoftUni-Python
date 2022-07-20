# import re

# text= input()
#
# expression = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
# matches = re.finditer(expression, text)
#
# output = list()
# for match in matches:
#     output.append(match.group())
#
# print(" ".join(output))




# pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
# text = input()
#
# valid_nums = re.finditer(pattern, text)
# valid_nums = [num.group() for num in valid_nums]
# print(*valid_nums)




import re

pattern = "(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
numbers = input()
matches = re.finditer(pattern, numbers)

for match in matches:
    print(match.group(), end=" ")