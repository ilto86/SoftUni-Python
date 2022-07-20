# # 'w' - create file or overwrite file
# import time
# from os import linesep
#
# # linesep -> '\n' for Unix/Linux, '\n\r' for Windows
#
# file = open('../files/w_demos.txt', 'w')
# file.write('--- w ---')
# file.write(linesep)
# file.write('It works!')
# file.write(linesep)
# file.write(str(time.time()))
# file.write(linesep)


with open("my_first_file.txt", "w") as file:
    file.writelines("I just created my first file!")

with open("my_first_file.txt", "a") as file:
    file.writelines("\nI just created my second line!")