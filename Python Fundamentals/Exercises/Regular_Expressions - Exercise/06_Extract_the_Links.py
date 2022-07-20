import re

text = input()
valid_links = []
pattern = r'((www)\.([a-zA-Z0-9-]+)(\.[a-z]+)(\.[a-z]+)*)'

while text:
    matches = re.finditer(pattern, text)

    for match in matches:
        valid_links.append(match.group(1))

    text = input()

for valid_link in valid_links:
    print(valid_link)





# import re
#
# pattern = r"((www)\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+))"
# some_text = input()
# valid_links = []
# while some_text:
#     matches = re.finditer(pattern, some_text)
#     for match in matches:
#         valid_links.append(match.group(1))
#     some_text = input()
# for valid_link in valid_links:
#     print(valid_link)





# import re
#
# pattern = r"\b(?P<url>www.[A-Za-z0-9]+[/-A-Za-z0-9]*\.[a-z]+[a-z\.]*)\b"
# links_list = []
#
# while True:
#     text = input()
#
#     if text == "":
#         break
#
#     matches = re.finditer(pattern, text)
#
#     for match in matches:
#         links_list.append(match.group("url"))
#
# for url in links_list:
#     print(url)