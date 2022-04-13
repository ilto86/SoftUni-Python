# words = input()
#
# result = [index for index in range(len(words)) if words[index].isupper()]
#
# print(result)

# str = input()
# capitals = []
# for idx, chr in enumerate(str):
#     if 65 <= ord(chr) <= 90:
#         capitals.append(idx)
# print(capitals)

# word = input()
#
# array_ch = []
#
# for position, ch in enumerate(word):
#     if 65 <= ord(ch) <= 90:
#         array_ch.append(position)
#
# print(array_ch)

# word = input()
#
# capital_letter_idx = []
#
# for idx,letter in enumerate(word):
#     if 65 <= ord(letter) <= 90:
#         capital_letter_idx.append(idx)
#
# print(capital_letter_idx)

string = input()
string = list(string)
new_list = []
upper_index = 0
for i in string:

    if i.isupper():
        index = string.index(i)
        if index in new_list:
            index = upper_index
        new_list.append(index)
    upper_index += 1
print(new_list)