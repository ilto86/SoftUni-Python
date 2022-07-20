# sublists = input().split("|")
#
# result = []
#
# for idx in range(len(sublists) - 1, -1, -1):
#     current_elements = sublists[idx].strip().split()
#     result.extend(current_elements)
#
# print(' '.join(result))






numbers_string = input().split("|")
flatten_list = list()

for num in range(len(numbers_string) - 1, -1, -1):
    current_elements = numbers_string[num].strip().split()
    flatten_list.extend(current_elements)

print(' '.join(flatten_list))