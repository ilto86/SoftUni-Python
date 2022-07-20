text = input()

while text != "end":
    reversed_text = ""
    for char in reversed(text):
        reversed_text += char
    print(text + " = " + reversed_text)

    text = input()




# text = input()
#
# while text != "end":
#     rev = reversed(text)
#     reversed_text = ""
#     for char in rev:
#         reversed_text += char
#     print(f"{text} = {reversed_text}")
#
#     text = input()




# text = input()
#
# while text != "end":
#     rev = reversed(text)
#     reversed_text = "".join(rev)
#     print(f"{text} = {reversed_text}")
#
#     text = input()




# text = input()
# new_text = ""
#
# while text != "end":
#     new_text = text[::-1]
#     print(f"{text} = {new_text}")
#
#     text = input()



word = input()

while not word == "end":
    print(f"{word} = {word[::-1]}")
    word = input()