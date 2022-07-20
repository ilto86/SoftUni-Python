# banned = input().split(", ")
# text = input()
#
# for word in banned:
#     while word in text:
#         text = text.replace(word, "*" * len(word))
# print(text)


banned_words = input().split(", ")
text = input()

for banned_word in banned_words:
    text = text.replace(banned_word, "*" * len(banned_word))

print(text)