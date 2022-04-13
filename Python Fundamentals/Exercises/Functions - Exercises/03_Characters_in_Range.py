# def get_symbols(first, second):
#     collected_symbols = []
#     # current_symbols = [ord(x), ord(y) for x, y in first_string + 1, second_string]
#     for current_symbol in range(ord(first) + 1, ord(second)):
#         collected_symbols.append(chr(current_symbol))
#
#     return collected_symbols
#
# first_string = input()
# second_string = input()
# result = get_symbols(first_string, second_string)
# print(' '.join(result))



def char_in_range(ch1, ch2):
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end=' ')


char1 = input()
char2 = input()
char_in_range(char1, char2)



# def char_in_range(ch1, ch2):
#     result = []
#     for i in range(ord(ch1) + 1, ord(ch2)):
#         result.append(chr(i))
#
#     return ' '.join(result)
#
# char1 = input()
# char2 = input()
# print(char_in_range(char1, char2))