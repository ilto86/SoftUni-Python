rows, cols = [int(x) for x in input().split()]
word = input()

idx = 0

for row in range(rows):
    elements = [None] * cols
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols -1, -1, -1)
    for col in range(start, end, step): # (0, cols, 1)
        elements[col] = word[idx % len(word)]
        idx += 1
    print("".join(elements))







# rows, cols = [int(x) for x in input().split()]
# word = input()
#
# idx = 0
#
# for row in range(rows):
#     elements = [None] * cols
#     if row % 2 == 0:
#         for col in range(cols): # (0, cols, 1)
#             elements[col] = word[idx % len(word)]
#             idx += 1
#     else:
#         for col in range(cols - 1, -1, -1):
#             elements[col] = word[idx % len(word)]
#             idx += 1
#     print("".join(elements))




# rows, cols = [int(x) for x in input().split()]
# word = input()
# idx = 0
#
# for row in range(rows):
#     row_elements = []
#     for col in range(cols):
#         row_elements.append(word[idx % len(word)])
#         idx += 1
#     if row % 2 == 0:
#         print(*row_elements, sep="")
#     else:
#         print(*reversed(row_elements), sep="")





# rows, cols = [int(x) for x in input().split()]
# word = input()
# idx = 0
#
# for row in range(rows):
#     row_elements = ""
#     for col in range(cols):
#         row_elements += word[idx % len(word)]
#         idx += 1
#     if row % 2 == 0:
#         print(row_elements)
#     else:
#         print(row_elements[::-1])






# rows, cols = [int(x) for x in input().split()]
# word = input()
# idx = 0
#
# for row in range(rows):
#     row_elements = [None] * cols
#     if row % 2 == 0:
#         for col in range(cols):
#             row_elements[col] = word[idx % len(word)]
#             idx += 1
#     else:
#         for col in range(cols - 1, -1, -1):
#             row_elements[col] = word[idx % len(word)]
#             idx += 1
#     print(*row_elements, sep="")



# from math import ceil
#
# rows, cols = [int(x) for x in input().split()]
# word = input()
# word = word * ceil(rows * cols / len(word))
#
# for row in range(rows):
#     current_word = word[:cols]
#     word = word[cols:]
#     if row % 2 == 0:
#         print(current_word)
#     else:
#         print(current_word[::-1])