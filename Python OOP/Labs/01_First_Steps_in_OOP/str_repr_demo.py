values = [
    # [1, 2, 3, 4, 5],
    # {1, 2, 3, 4, 5},
    # {'a': 1, 'b': 2},
    'Text', "Some_Text", "Another_Text"
]

[print(str(x)) for x in values]

print("\n","#" * 20)
print("#" * 20, "\n")

[print(repr(x)) for x in values]