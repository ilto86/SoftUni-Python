def reverse_text(text):
    index = 0
    n = len(text)
    while index < n:
        yield text[n - index - 1]
        index += 1


for char in reverse_text("step"):
    print(char, end='')

print()

for char in reverse_text("repoleveD nohtyP doog a ma I"):
    print(char, end='')
