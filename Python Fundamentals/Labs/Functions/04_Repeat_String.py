# repeater = lambda str, count: str * count
#
# current_string = input()
# current_count = int(input())
#
# print(repeater(current_string, current_count))


def repeat_string(string, n):
    return string * n

text = input()
count = int(input())
print(repeat_string(text, count))