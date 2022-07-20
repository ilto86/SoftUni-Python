# import re
#
#
# def read_words():
#     with open('./words_count_files/words.txt', 'r') as file:
#         return file.read().split(' ')
#
#
# def count_words_in_file(words):
#     words_counts = {
#         word: 0 for word in words
#     }
#
#     with open('./words_count_files/input.txt', 'r') as file:
#         for line in file:
#             words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', line)]
#             for word in words:
#                 words_counts[word] += words_in_line.count(word.lower())
#     return words_counts
#
#
# words_counts = count_words_in_file(read_words())
# words_counts_sorted = sorted(words_counts.items(),
#                              key=lambda x: x[1],
#                              reverse=True)
# [
#     print(f'{w} - {c}') for w, c in words_counts_sorted
# ]




# Option one not simple regex
# import re
# import string
#
# print(list(string.punctuation))
# with open("words.txt") as file:
#     searched_words = file.read().split()
#
#
# occs = {}
#
# with open("input.txt") as file:
#     content = file.read().lower()
#     for s_word in searched_words:
#         result = re.findall(rf"(?<=(\-|\s)){word}(?=(\.|))", content)
#         occs[s_word] = len(result)
#
# sorted_result = sorted(occs.items(), key=lambda x: -x[1])
# for key, value in sorted_result:
#     print(f"{key} - {value}")




#Option two simple regex

# def get_file_content(path):
#     with open(path, 'r') as data:
#         data = ''.join(data.readlines())
#         return pattern.findall(data.lower())
#
# def write_to_file(data):
#     for k, v in data:
#         output_data = f'{k} - {v}'
#         with open('output.txt', 'a') as file:
#             file.write(output_data)
#             file.write("\n")
#
#
# import re
# pattern = re.compile(r"[a-zA-Z\']+")
#
# path_to_words = 'words.txt'
# path_to_input = 'input.txt'
#
# get_words = get_file_content(path_to_words)
# get_text = get_file_content(path_to_input)
#
# my_dect = {word:get_text.count(word) for word in get_words if word in get_text}
# sorted_list = sorted(my_dect.items(), key=lambda x: -x[1])
#
# write_to_file(sorted_list)





# import re
#
#
# searched_words = []
# with open("words.txt") as file:
#     searched_words = file.read().split()
#
# words_count = {}
# with open("input.txt") as file:
#     text = file.read()
#     for word in searched_words:
#         pattern = fr"\b{word}\b"
#         count = len(re.findall(pattern, text, re.IGNORECASE))
#         words_count[word] = count
#
# with open("output.txt", "w") as file:
#     sorted_result = sorted(words_count.items(), key=lambda kvpt: -kvpt[1])
#     for key, value in sorted_result:
#             file.writelines(f"{key} - {value}\n")





import re


def read_searched_words(file_path):
    searched_words = []
    with open(file_path) as file:
        searched_words = file.read().split()
    return searched_words


def calculate_words_count(searched_words, file_path):
    words_count = {}
    with open(file_path) as file:
        text = file.read()
        for word in searched_words:
            pattern = fr"\b{word}\b"
            count = len(re.findall(pattern, text, re.IGNORECASE))
            words_count[word] = count
    return words_count


def store_result(result, output_file_path):
    with open(output_file_path, "w") as file:
        sorted_result = sorted(result.items(), key=lambda kvpt: -kvpt[1])
        for key, value in sorted_result:
                file.writelines(f"{key} - {value}\n")


words = read_searched_words(".\words_count_files\words.txt")
result = calculate_words_count(words, ".\words_count_files\input.txt")
store_result(result, ".\words_count_files\output.txt")



# import os
#
#
# absolute_path = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(absolute_path, "words_count_files", "input.txt")
#
# print(file_path)