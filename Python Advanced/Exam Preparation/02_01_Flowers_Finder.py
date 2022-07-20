from collections import deque

vowels = deque([x for x in input().split()])
consonants = [x for x in input().split()]

flowers = {
    "rose": set("rose"),
    "tulip": set("tulip"),
    "lotus": set("lotus"),
    "daffodil": set("daffodil")
}

founded_flower = ""
found_flower = False
while not found_flower and vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for key, value in flowers.items():
        if vowel in value:
            value.remove(vowel)
        if consonant in value:
            value.remove(consonant)
        if len(value) == 0:
            founded_flower = key
            found_flower = True
            break

if found_flower:
    print(f"Word found: {founded_flower}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")