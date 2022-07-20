# from os import remove
# from os.path import exists
#
# file_path = './files/to_delete.txt'
#
# # open(file_path, 'w').close()
# if exists(file_path):
#     remove(file_path)
#     print('File deleted')
# else:
#     print('File already deleted')


import os

try:                                    # if os.path.exists("my_first_file.txt"):
    os.remove("my_first_file.txt")      #     os.remove("my_first_file.txt")
except FileNotFoundError:               # else:
    print("File already deleted!")      #     print("File already deleted!")

if os.path.exists("my_first_file.txt"):  # try:
    os.remove("my_first_file.txt")       #     os.remove("my_first_file.txt")
else:                                    # except FileNotFoundError:
    print("File already deleted!")       #     print("File already deleted!")