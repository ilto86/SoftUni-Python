# import re
#
# data = input()
# pattern = r'\b_[a-zA-Z0-9]+\b'
#
# result = re.findall(pattern, data)
#
# words_list = []
#
# for word in result:
#     words_list.append(word[1:])
#
# print(','.join(words_list))



import re

test_str = input()
regex = r'\b_[a-zA-Z0-9]+\b'

matches = re.finditer(regex, test_str, re.MULTILINE)

words_list = []
for match in matches:
    words_list.append(match[0])

last_matches = ','.join(words_list)
last_matches = last_matches.replace("_", "")
print(last_matches)