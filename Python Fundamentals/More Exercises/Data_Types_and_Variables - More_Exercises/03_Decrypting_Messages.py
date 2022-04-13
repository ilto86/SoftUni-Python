key = int(input())
n_lines = int(input())
word = ""

for n in range(n_lines):
    letter = input()
    character = ord(letter) + key
    word += chr(character)

print(word)