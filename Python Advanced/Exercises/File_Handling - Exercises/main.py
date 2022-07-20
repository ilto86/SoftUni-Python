# from os import listdir
#
# print(listdir('./'))



from os import listdir
from os.path import isdir, join

import files as files


def directory_traversal(path, files_by_ext):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), files_by_ext)
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


result = {}
directory_traversal('./', result)

sorted_result = {x: y for x, y in sorted(result.items(), key=lambda k: (len(k[1]), k[0], k[1]))}
for ext, files in sorted_result.items():
    print(f'.{ext}' + '\n')
    for file in sorted(files):
       print(f'- - - {file}\n')




# from os import walk
#
#
# for root, dirs, files in walk('.'):
#     print(root)
#     print(dirs)
#     print(files)

