# chars = input().split(", ")
# print({char: ord(char) for char in chars})



# print({char: ord(char) for char in input().split(', ')})



# characters = input().split(", ")
# char_dict = dict()
#
# for char in characters:
#     char_dict[char] = ord(char)
# print(char_dict)



characters = input().split(", ")
char_dict = {char: ord(char) for char in characters}
print(char_dict)