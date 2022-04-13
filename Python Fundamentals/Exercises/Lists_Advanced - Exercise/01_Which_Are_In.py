text1 = input().split(", ")
text2 = input().split(", ")
text1_in_text2 = list()

for i in text1:
    list = i
    for el in text2:
        if i in text2[text1]:
            text1_in_text2.append(el)
        else:
            continue
print(text1_in_text2)

# text1_in_text2 = [i for i in text1 for el in text2 if i in el]
# print(sorted(set(text1_in_text2), key=text1_in_text2.index))


substrings = input().split(", ")
sentence = input()
result = [el for el in substrings if el in sentence]
print(result)




