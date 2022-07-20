# first = input()
# second = input()
#
# while first in second:
#     second = second.replace(first, "")
# print(second)



# search = input()
# text = input()
#
# # isPresent = search in text
# while search in text:
#     text = text.replace(search, "")
#
# print(text)



substring_to_remove = input()
word = input()

# isPresent = search in text
while substring_to_remove in word:
    word = word.replace(substring_to_remove, "")

print(word)