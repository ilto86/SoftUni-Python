n = int(input())
searched_word = input()

all_words = []
matched_words = []

for _ in range(n):
    current_word = input()
    all_words.append(current_word)
    if searched_word in current_word:
        matched_words.append(current_word)

print(all_words)
print(matched_words)



# n = int(input())
# word = input()
# strings = []
#
# for _ in range(n):
#     current_string = input()
#     strings.append(current_string)
# print(strings)
# for i in range(len(strings) - 1, -1, -1):
#     element = strings[i]
#     if word not in element:
#         strings.remove(element)
# print(strings)