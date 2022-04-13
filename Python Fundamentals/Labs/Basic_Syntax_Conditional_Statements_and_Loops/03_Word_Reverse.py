# word = input()
# reversed_word = ""
#
# for i in range(len(word) -1, -1, -1):
#     reversed_word += word[i]
# print(reversed_word)



# word = input()
# for i in range(len(word) -1, -1, -1):
#     print(word[i], end='')



# word = input()
# print(word[::-1])



word = input()
new_word = ""

for letter in word:
    new_word = letter + new_word

print(new_word)