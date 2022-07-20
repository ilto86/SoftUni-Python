# string = list(input())
#
# while string:
#     print(string.pop(), end="")




# text = list(input())
#
# while text:
#     print(text.pop(), end="")




string = list(input())

reversed_string = []

while string:
    reversed_string.append(string.pop())

print("".join(reversed_string))