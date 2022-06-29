# text = input()
# vowels_not_included = ['a', 'o', 'u', 'e', 'i']
# no_vowels = []

# for str in text:
#     if str.lower() not in vowels_not_included:
#         no_vowels.append(str)

# print("".join(no_vowels))




vowels = ["a", "o", "u", "e", "i"]
text = input().lower()
no_vowels_text = [ch for ch in text if ch not in vowels]

print("".join(no_vowels_text))
