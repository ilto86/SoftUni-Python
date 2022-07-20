from os import listdir
from os.path import isdir, join


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
sorted_result = {key: value for key, value in sorted(result.items(), key=lambda kvpt: (len(kvpt[1]), kvpt[0], kvpt[1]))}
with open('./report.txt', 'w') as output_file:
    for ext, files in result.items():
        output_file.write(f".{ext}" + '\n')
        for file in files:
            output_file.write(f'- - - {file}\n')