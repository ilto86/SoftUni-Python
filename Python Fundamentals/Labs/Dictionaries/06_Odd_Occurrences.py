# words = input().split()
# dict = {}
#
# for word in words:
#     word_lower = word.lower()
#     if word_lower not in dict:
#         dict[word_lower] = 0
#     dict[word_lower] += 1
#
# odd_dictionary = {key: value for key, value in dict.items() if value % 2 != 0}
# print(" ".join(odd_dictionary))



# words = input().split()
# dictionary = {}
#
# for word in words:
#     word_lower = word.lower()
#     if word_lower not in dictionary:
#         dictionary[word_lower] = 0
#     dictionary[word_lower] += 1
#
# for (key, value) in dictionary.items():
#     if value % 2 != 0:
#         print(key, end=" ")


# Java C# PHP PHP JAVA C java
# 3 5 5 hi pi HO Hi 5 ho 3 hi pi
# a a A SQL xx a xx a A a XX c


words = input().split()
words = list(map(lambda w: w.lower(), words))
ocurrences = dict()

for word in words:
    if word not in ocurrences:
        ocurrences[word] = 1
    else:
        ocurrences[word] += 1

odd_words = list()

for word in ocurrences.keys():
    if ocurrences[word] % 2 != 0:
        odd_words.append(word)
print(" ".join(odd_words))