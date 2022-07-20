def words_sorting(*args):
    words = {}
    for word in args:
        ascii_values_sum = 0
        for letter in word:
            ascii_values_sum += ord(letter)
        words[word] = ascii_values_sum
    sum_result = sum(words.values())

    if sum_result % 2 == 0:
        sorted_words = sorted(words.items(), key=lambda x: x[0])
    else:
        sorted_words = sorted(words.items(), key=lambda x: -x[1])

    result = ""
    for k,v in sorted_words:
        result += f"{k} - {v}\n"

    return result


print(words_sorting('escape', 'charm', 'mythology'))    # charm - 523
                                                        # escape - 625
                                                        # mythology - 1004

print(words_sorting('escape', 'charm', 'eye'))          # escape - 625
                                                        # charm - 523
                                                        # eye - 323

print(
 words_sorting('cacophony', 'accolade'))                # accolade - 812
                                                        # cacophony - 964



# def words_sorting(*args):
#     result_dict = {}
#     for word in args:
#         result = 0
#         for el in word:
#             result += ord(el)
#         result_dict[word] = result
#
#     words = ""
#     if sum(result_dict.values()) % 2 == 0:
#         for word in sorted(result_dict.items(), key=lambda x: x[0]):
#             words += f"{word[0]} - {word[1]}" + "\n"
#         return words
#     else:
#         for word in sorted(result_dict.items(), key=lambda x: -x[1]):
#             words += f"{word[0]} - {word[1]}" + "\n"
#         return words
#
#
# print(
#  words_sorting(
#  'escape',
#  'charm',
#  'mythology'
#  ))
#
# print(
#  words_sorting(
#  'escape',
#  'charm',
#  'eye'
#  ))
#
# print(
#  words_sorting(
#  'cacophony',
#  'accolade'
#  ))