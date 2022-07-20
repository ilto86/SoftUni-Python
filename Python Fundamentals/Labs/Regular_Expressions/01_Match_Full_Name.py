import re

# text = input()
#
# matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)
#
# print(" ".join(matches))
#
# matches = re.search(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)
# print(matches.group())

# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# text = input()
#
# valid_names = re.findall(pattern, text)

# print(*valid_names)  # print(" ".join(valid_names))

import re

text = input()

pattern = r"\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b"      # "\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(pattern, text)

print(" ".join(matches))