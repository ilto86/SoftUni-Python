import re

pattern = r'\d+'

while True:
    text = input()

    if not text:
        break

    result = re.findall(pattern, text)

    if len(result) > 0:
        print(" ".join(result), end=" ")



# import re
#
# regex = r'\d+'
#
# while True:
#     test_str = input()
#
#     if not test_str:
#         break
#
#     matches = re.finditer(regex, test_str, re.MULTILINE)
#
#     for matchNum, match in enumerate(matches, start=1):
#         print(match[0], end=' ')