# import re
#
# text = input()
#
# pattern = r"(#|@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
#
# matches = re.finditer(pattern, text)
#
# valid_pairs_count = []
# mirror_words = []
#
# for match in matches:
#     valid_pairs_count.append(match[2])
#     matched =  match[3][::-1]
#     if match[2] == matched:
#         mirror_words.append(match[2] + " <=> " + match[3])
#
# if len(valid_pairs_count) == 0:
#     print("No word pairs found!")
# else:
#     print(f"{len(valid_pairs_count)} word pairs found!")
#
# if len(mirror_words) == 0:
#     print("No mirror words!")
# else:
#     print("The mirror words are:")
#     print(", ".join(mirror_words))





import re

pattern = r"(#|@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
text = input()
matches = re.findall(pattern, text)
mirror_words = []

matched_words = [el for el in matches]
if matched_words:
    print(f"{len(matched_words)} word pairs found!")
else:
    print("No word pairs found!")

for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(match[1] + " <=> " + match[2])

if mirror_words:
    print("The mirror words are: ")
    print(f"{', '.join(mirror_words)}")
else:
    print("No mirror words!")