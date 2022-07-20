# file_path = './text.txt' # File found
# # file_path = './text2.txt'  # File not found
#
# try:
#     open(file_path, 'r')
#     print('File found')
# except FileNotFoundError:
#     print('File not found')

# try:
#     file = open("text.txt")
#     print('File found')
# except FileNotFoundError:
#     print("File not found")


import os

if os.path.exists("text.txt"):
    print('File found')
else:
    print("File not found")

