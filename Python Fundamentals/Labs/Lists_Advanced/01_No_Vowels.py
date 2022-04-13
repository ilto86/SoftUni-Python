# vowels = ["a", "o", "u", "e", "i"]
# text = input().lower()
# no_vowels_text = list()
#
# for ch in text:
#     if ch not in vowels:
#         no_vowels_text.append(ch)
#
# print("".join(no_vowels_text))



# vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
# text = input()
# no_vowels_text = [ch for ch in text if ch not in vowels]
#
# print("".join(no_vowels_text))




# vowels = ["a", "o", "u", "e", "i"]
# text = input().lower()
# no_vowels_text = [ch for ch in text if ch not in vowels]
#
# print("".join(no_vowels_text))

# def vowels(word):
#     no_vowels_text = [str for str in word if str.lower() not in ["a", "o", "u", "e", "i"]]
#     print("".join(no_vowels_text))
#
# # vowels(input())
# text = input()   # vowels(input())
# vowels(text)     # vowels(input())


text = input()
vowels_not_included = ['a', 'o', 'u', 'e', 'i']
no_vowels = []

for str in text:
    if str.lower() not in vowels_not_included:
        no_vowels.append(str)

print("".join(no_vowels))