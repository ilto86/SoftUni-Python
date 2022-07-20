# morse_code = {
# 	".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
# 	".": "E", "..-.": "F", "--.": "G", "....": "H",
# 	"..": "I", ".---": "J", "-.-": "K", ".-..": "L",
# 	"--": "M", "-.": "N", "---": "O", ".--.": "P",
# 	"--.-": "Q", ".-.": "R", "...": "S", "-": "T",
# 	"..-": "U", "...-": "V", ".--": "W", "-..-": "X",
# 	"-.--": "Y", "--..": "Z", "|": " "
# }
#
# print("".join([morse_code[char] for char in input().split()]))






# MORSE_CODE_DICT = {'..-.': 'F', '-..-': 'X',
#                  '.--.': 'P', '-': 'T', '..---': '2',
#                  '....-': '4', '-----': '0', '--...': '7',
#                  '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
#                  '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
#                  '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
#                  '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
#                  '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
#                  '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}
#
# initial_text = input().split()
#
# new_text = []
#
# for i in initial_text:
#     if i == "|":
#         i = i.replace('|', '')
#     new_text.append(i)
#
#
# cypher = ''
#
# for letter in new_text:
#     if letter != '':
#         cypher += MORSE_CODE_DICT[letter]
#     else:
#         cypher += ' '
# print(cypher)





morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
              '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
              '--..': 'Z'}

text = input()
word = ''
for el in text:
    if not el == '|':
        word += el
    else:
        word = word.split()
        for i in word:
            print(morse_code[i], end='')
        print(' ', end='')
        word = ''
word = word.split()
for i in word:
    print(morse_code[i], end='')
print()





# MORSE_CODE_SYMBOLS_TO_LETTERS = {'.-': 'A', '-...': 'B', '-.-.': 'C',
#                     '-..': 'D', '.': 'E', '..-.': 'F',
#                     '--.': 'G', '....': 'H', '..': 'I',
#                     '.---': 'J', '-.-': 'K', '.-..': 'L',
#                     '--': 'M', '-.': 'N', '---': 'O',
#                     '.--.': 'P', '--.-': 'Q', '.-.': 'R',
#                     '...': 'S', '-': 'T', '..-': 'U',
#                     '...-': 'V', '.--': 'W', '-..-': 'X',
#                     '-.--': 'Y', '--..': 'Z'
#                 }
#
# def find_eng_word(code, MORSE_CODE_SYMBOLS_TO_LETTERS):
#     morse_symbols = code.split()
#     eng_word = ""
#     for symbol in morse_symbols:
#         eng_word += MORSE_CODE_SYMBOLS_TO_LETTERS[symbol]
#     return eng_word
#
# def decrypt_message(msg, MORSE_CODE_SYMBOLS_TO_LETTERS):
#     result = []
#     for morse_code in msg:
#         eng_word = find_eng_word(morse_code, MORSE_CODE_SYMBOLS_TO_LETTERS)
#         result.append(eng_word)
#     return result
#
# def print_result(decrypted_message):
#     return print(" ".join(decrypted_message))
#
#
# message = input().split(" | ")
# decrypted_message = decrypt_message(message, MORSE_CODE_SYMBOLS_TO_LETTERS)
# print_result(decrypted_message)





# def decode_morse(morse_word: str) -> str:
#     """Decode morse text, according to the problem description.
#     Args:
#         morse_word (str): The word to be decrypted.
#     Returns:
#         str: Decrypted word.
#     """
#
#     codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
#              '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
#     chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     morse_dict = {code: char for code, char in zip(codes, chars)}
#
#     decoded_word = ''
#     for code in morse_word.split():
#         decoded_word += morse_dict[code]
#     return decoded_word
#
#
# data = input().split('|')
# decoded_text = []
# for morse_word in data:
#     morse_word = morse_word.strip()
#     decoded_text.append(decode_morse(morse_word))
# print(' '.join(decoded_text))