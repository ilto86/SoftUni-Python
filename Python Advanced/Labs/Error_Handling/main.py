'''
                               Python Advanced Retake Exam - 14 April 2022
'''
# 01. Ramen Shop

# from collections import deque
#
# bowls_ramen = deque([int(x) for x in input().split(", ")])
# customers = deque([int(x) for x in input().split(", ")])
#
# while bowls_ramen and customers:
#     cup_ramen = bowls_ramen[-1]
#     customer = customers[0]
#
#     if cup_ramen > customer:
#         result = cup_ramen - customer
#         customers.popleft()
#         bowls_ramen.pop()
#         bowls_ramen.append(result)
#     elif customer > cup_ramen:
#         result = customer - cup_ramen
#         bowls_ramen.pop()
#         customers.popleft()
#         customers.appendleft(result)
#     else:
#         bowls_ramen.pop()
#         customers.popleft()
#
# if not customers:
#     print("Great job! You served all the customers.")
#     if bowls_ramen:
#         print(f"Bowls of ramen left: {', '.join(map(str, bowls_ramen))}")
# else:
#     print("Out of ramen! You didn't manage to serve all customers.")
#     print(f"Customers left: {', '.join(map(str, customers))}")



'''
                               Python Advanced Retake Exam - 14 April 2022
'''
# 02. Martian Explorer

# def get_position(command, row, col):
#     if command == "up":
#         return row - 1, col
#     if command == "down":
#         return row + 1, col
#     if command == "left":
#         return row, col - 1
#     if command == "right":
#         return row, col + 1
#
#
# def get_is_outside(row, col, size):
#     result = tuple()
#     if row < 0:
#         row = size - 1
#         result = row, col
#     if row >= size:
#         row = 0
#         result = row, col
#     if col < 0:
#         col = size - 1
#         result = row, col
#     if col >= size:
#         col = 0
#         result = row, col
#     return result
#
#
# size = 6
# matrix = []
# rover_row = 0
# rover_col = 0
# water = 0
# concrete = 0
# metal = 0
#
# for next_row in range(size):
#     row_elements = input().split()
#     for next_col in range(size):
#         if row_elements[next_col] == "E":
#             rover_row = next_row
#             rover_col = next_col
#     matrix.append(row_elements)
#
# commands = input().split(", ")
#
#
# for command in commands:
#
#     next_row, next_col = get_position(command, rover_row, rover_col)
#
#     if 0 > next_row or next_row >= size or 0 > next_col or next_col >= size:
#         next_row, next_col = get_is_outside(next_row, next_col, size)
#
#
#     if matrix[next_row][next_col] == "W":
#         water += 1
#         matrix[next_row][next_col] = "-"
#         print(f"Water deposit found at ({next_row}, {next_col})")
#     elif matrix[next_row][next_col] == "C":
#         concrete += 1
#         matrix[next_row][next_col] = "-"
#         print(f"Concrete deposit found at ({next_row}, {next_col})")
#     elif matrix[next_row][next_col] == "M":
#         metal += 1
#         matrix[next_row][next_col] = "-"
#         print(f"Metal deposit found at ({next_row}, {next_col})")
#     elif matrix[next_row][next_col] == "R":
#         print(f"Rover got broken at ({next_row}, {next_col})")
#         break
#
#     rover_row, rover_col = next_row, next_col
#
# if water > 0 and  concrete > 0 and metal > 0:
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")



'''
                               Python Advanced Retake Exam - 14 April 2022
'''
# 03. Words Sorting


# def words_sorting(*args):
#     result_dict = {}
#     for word in args:
#         result = 0
#         for el in word:
#             result += ord(el)
#         result_dict[word] = result
#
#     words = ""
#     if sum(result_dict.values()) % 2 != 0:
#         for word in sorted(result_dict.items(), key=lambda x: -x[1]):
#             words += (f"{word[0]} - {word[1]}") + "\n"
#         return words
#     else:
#         for word in sorted(result_dict.items(), key=lambda x: x[0]):
#             words += f"{word[0]} - {word[1]}" + "\n"
#         return words
#
#
# print(words_sorting('escape', 'charm', 'mythology'))
# print(words_sorting('escape', 'charm', 'eye'))
# print(words_sorting('cacophony', 'accolade'))





'''
                                Python Advanced Exam - 19 February 2022
'''
# 01. Flowers Finder
# from collections import deque
#
#
# flowers = {
#     "rose": ["r", "o", "s", "e"],
#     "tulip": ["t", "u", "l", "i", "p"],
#     "lotus": ["l", "o", "t", "u", "s"],
#     "daffodil": ["d", "a", "f", "o", "i", "l"]
# }
#
# vowels = deque(input().split())
# consonants = deque(input().split())
# found_flower = False
# word_found = []
#
# while not found_flower and vowels and consonants:
#     vowel_letter = vowels.popleft()
#     consonant_letter = consonants.pop()
#
#     for key, value in flowers.items():
#         if vowel_letter in value:
#             value.remove(vowel_letter)
#         if consonant_letter in value:
#             value.remove(consonant_letter)
#         if len(value) == 0:
#             word_found.append(key)
#             found_flower = True
#             break
#
# if word_found:
#     print(f"Word found: {''.join(word_found)}")
# else:
#     print("Cannot find any word!")
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")



'''
                                Python Advanced Exam - 19 February 2022
'''
# 02. Pawn Wars

# def move_white_pawn(row, col):
#     if 0 <= row - 1:
#         return row - 1, col
#
#
# def move_black_pawn(row, col, size):
#     if row + 1 < size:
#         return row + 1, col
#
#
# def square_position(col, row):
#     result = []
#     if col == 0:
#         result.append("a")
#     if col == 1:
#         result.append("b")
#     if col == 2:
#         result.append("c")
#     if col == 3:
#         result.append("d")
#     if col == 4:
#         result.append("e")
#     if col == 5:
#         result.append("f")
#     if col == 6:
#         result.append("g")
#     if col == 7:
#         result.append("h")
#     if row == 0:
#         result.append(8)
#     if row == 1:
#         result.append(7)
#     if row == 2:
#         result.append(6)
#     if row == 3:
#         result.append(5)
#     if row == 4:
#         result.append(4)
#     if row == 5:
#         result.append(3)
#     if row == 6:
#         result.append(2)
#     if row == 7:
#         result.append(1)
#     return result
#
#
# board_size = 8
# matrix = []
# game_over = False
# a_row = 0
# a_col = 0
#
# b_row = 0
# b_col = 0
#
# for row in range(board_size):
#     row_elements = input().split()
#     for col in range(board_size):
#         if row_elements[col] == "w":
#             a_row = row
#             a_col = col
#         elif row_elements[col] == "b":
#             b_row = row
#             b_col = col
#     matrix.append(row_elements)
#
# white_next_row, white_next_col = a_row, a_col
# black_next_row, black_next_col = b_row, b_col
#
# for _ in range(board_size):
#     matrix[white_next_row][white_next_col] = "-"
#     if 0 <= white_next_row - 1 and 0 <= white_next_col - 1:
#         if matrix[white_next_row - 1][white_next_col - 1]  == "b":
#             position = square_position(white_next_col - 1, white_next_row - 1)
#             print(f"Game over! White win, capture on {''.join([str(x) for x in position])}.")
#             break
#     if 0 <= white_next_row - 1 and white_next_col + 1 < board_size:
#         if matrix[white_next_row - 1][white_next_col + 1]  == "b":
#             position = square_position(white_next_col + 1, white_next_row - 1)
#             print(f"Game over! White win, capture on {''.join([str(x) for x in position])}.")
#             break
#     if white_next_row == 0:
#         position = square_position(white_next_col, white_next_row)
#         print(f"Game over! White pawn is promoted to a queen at {''.join([str(x) for x in position])}.")
#         break
#     white_next_row, white_next_col = move_white_pawn(white_next_row, white_next_col)
#     matrix[white_next_row][white_next_col] = "w"
#
#     matrix[black_next_row][black_next_col] = "-"
#     if black_next_row + 1 < board_size and 0 <= black_next_col - 1:
#         if matrix[black_next_row + 1][black_next_col - 1] == "w":
#             position = square_position(black_next_col - 1, black_next_row + 1)
#             print(f"Game over! Black win, capture on {''.join([str(x) for x in position])}.")
#             break
#     if black_next_row + 1 < board_size and black_next_col + 1 < board_size:
#         if matrix[black_next_row + 1][black_next_col + 1] == "w":
#             position = square_position(black_next_col + 1, black_next_row + 1)
#             print(f"Game over! Black win, capture on {''.join([str(x) for x in position])}.")
#             break
#     if black_next_row == board_size - 1:
#         position = square_position(black_next_col, black_next_row)
#         print(f"Game over! Black pawn is promoted to a queen at {''.join([str(x) for x in position])}.")
#         break
#     black_next_row, black_next_col = move_black_pawn(black_next_row, black_next_col, board_size)
#     matrix[black_next_row][black_next_col] = "b"



'''
                                Python Advanced Exam - 19 February 2022
'''
# 03. Springtime

# def start_spring(**kwargs):
#     result = ''
#     spring = {}
#     for value, key in kwargs.items():
#         if key not in spring:
#             spring[key] = [value]
#         else:
#             spring[key].append(value)
#
#     sorted_spring = sorted(spring.items(), key=lambda x: (-len(x[1]), x[0]))
#     for tuple_ in sorted_spring:
#         type_name = tuple_[0]
#         objects_name = tuple_[1]
#         sorted_objects = sorted(objects_name)
#         result += f"{type_name}:\n"
#         for object in sorted_objects:
#             result += f"-{object}\n"
#
#     return result
#
# example_objects = {
#     "Swifts": "bird",
#     "Callery Pear": "tree",
#     "Water Lilly": "flower",
#     "Swallows": "bird",
#     "Dahlia": "flower",
#     "Tulip": "flower", }

# example_objects = {"Swallow": "bird",
#  "Thrushes": "bird",
#  "Woodpeckers": "bird",
#  "Swallows": "bird",
#  "Warblers": "bird",
#  "Shrikes": "bird",}

# example_objects = {"Magnolia": "tree",
#  "Swallow": "bird",
#  "Thrushes": "bird",
#  "Pear": "tree",
#  "Cherries": "tree",
#  "Shrikes": "bird",
#  "Butterfly": "insect"}


# print(start_spring(**example_objects))