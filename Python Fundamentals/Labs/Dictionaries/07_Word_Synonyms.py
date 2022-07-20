# n = int(input())
#
# synonym_dict = {}
#
# for _ in range(n):
#     word = input()
#     synonym = input()
#
#     if word not in synonym_dict:
#         synonym_dict[word] = []
#     synonym_dict[word].append(synonym)
#
# for key, value in synonym_dict.items():
#     print(f"{key} - {', '.join(value)}")




# n = int(input())
#
# synonym_dict = {}
#
# for _ in range(n):
#     word = input()
#     synonym = input()
#
#     if word not in synonym_dict:
#         synonym_dict[word] = []
#     synonym_dict[word].append(synonym)
#
# for key, value in synonym_dict.items():
#     print(f"{key} - {', '.join(value)}")




count = int(input())
dictionary = dict()

for i in range(count):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = list()

    dictionary[word].append(synonym)

for word in dictionary:
    synonyms = ", ".join(dictionary[word])
    print(f"{word} - {synonyms}")