# def is_inside(row, col, size):
#     if 0 <= row < size and 0 <= col < size:
#         return True
#     return False
#
#
# def get_chess_position(row, column):
#     row_names = [8, 7, 6, 5, 4, 3, 2, 1]
#     columns_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     return columns_names[column], row_names[row]
#
#
# matrix_size = 8
# matrix = []
#
# white_pawn = "w"
# black_pawn = "b"
#
# white_row, white_col = 0, 0
# black_row, black_col = 0, 0
#
# for row in range(matrix_size):
#     row_element = input().split()
#     for col in range(matrix_size):
#         if row_element[col] != "-":
#             if row_element[col] == white_pawn:
#                 white_row, white_col = row, col
#             else:
#                 black_row, black_col = row, col
#     matrix.append(row_element)
#
# current_row, current_col = white_row, white_col
# other_row, other_col = black_row, black_col
# current_player = white_pawn
# other_player = black_pawn
#
# is_capture = False
# is_queen = False
# position = tuple()
#
# while True:
#     next_row, next_col = current_row, current_col
#     next_player = current_player
#
#     if next_player == white_pawn:
#         if is_inside(next_row, next_col - 1, matrix_size) and matrix[next_row][next_col - 1] == black_pawn:
#             position = (next_row, other_col)
#             is_capture = True
#             break
#         elif is_inside(next_row, next_col + 1, matrix_size) and  matrix[next_row][next_col + 1] == black_pawn:
#             position = (next_row, other_col)
#             is_capture = True
#             break
#         elif current_row == 0:
#             position = (next_row, next_col)
#             is_queen = True
#             break
#         else:
#             matrix[next_row][next_col] = white_pawn
#             current_row, current_col = next_row - 1, next_col
#             current_row, other_row = other_row, current_row
#             current_col, other_col = other_col, current_col
#             current_player, other_player = other_player, current_player
#     else:
#         if is_inside(next_row, next_col - 1, matrix_size) and  matrix[next_row][next_col - 1] == white_pawn:
#             position = (next_row, other_col)
#             is_capture = True
#             break
#         elif is_inside(next_row, next_col + 1, matrix_size) and matrix[next_row][next_col + 1] == white_pawn:
#             position = (next_row, other_col)
#             is_capture = True
#             break
#         elif current_row == matrix_size - 1:
#             position = (next_row, next_col)
#             is_queen = True
#             break
#         else:
#             matrix[next_row][next_col] = black_pawn
#             current_row, current_col = next_row + 1, next_col
#             current_row, other_row = other_row, current_row
#             current_col, other_col = other_col, current_col
#             current_player, other_player = other_player, current_player
#
#
# player = 'White' if next_player == 'w' else 'Black'
# (column_name, row_name) = get_chess_position(*position)
# position_name = f'{column_name}{row_name}'
#
# if is_capture:
#     print(f'Game over! {player} win, capture on {position_name}.')
#
# if is_queen:
#     print(f'Game over! {player} pawn is promoted to a queen at {position_name}.')
#
# for row in matrix:
#     print(*row, sep=" ")






# def is_inside(row, col, size):
#     if 0 <= row < size and 0 <= col < size:
#         return True
#     return False
#
#
# def get_chess_position(row, column):
#     row_names = [8, 7, 6, 5, 4, 3, 2, 1]
#     columns_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     return columns_names[column], row_names[row]
#
#
# size = 8
# matrix = []
#
# white_pawn = "w"
# black_pawn = "b"
#
# white_row, white_col = 0, 0
# black_row, black_col = 0, 0
#
# for row in range(size):
#     row_element = input().split()
#     for col in range(size):
#         if row_element[col] != "-":
#             if row_element[col] == white_pawn:
#                 white_row, white_col = row, col
#             else:
#                 black_row, black_col = row, col
#     matrix.append(row_element)
#
# white_player_row, white_player_col = white_row, white_col
# black_player_row, black_player_col = black_row, black_col
# white_player = white_pawn
# black_player = black_pawn
# is_capture = False
# is_queen = False
# position = tuple()
#
# while not is_capture and not is_queen:
#     current_row, current_col = white_player_row, white_player_col
#     other_row, other_col = black_player_row, black_player_col
#     current_player = white_player
#     other_player = black_player
#
#     if current_player == white_pawn:
#         if is_inside(current_row, current_col - 1, size) and matrix[current_row][current_col - 1] == black_player:
#             matrix[current_row][other_col] = white_player
#             position = (current_row, other_col)
#             is_capture = True
#             break
#         elif is_inside(current_row, current_col + 1, size) and matrix[current_row][current_col + 1] == black_player:
#             matrix[current_row][other_col] = white_player
#             position = (current_row, other_col)
#             is_capture = True
#             break
#         elif current_row == 0:
#             matrix[current_row][current_col] = white_player
#             position = (current_row, current_col)
#             is_queen = True
#             break
#         else:
#             matrix[current_row][current_col] = white_player
#             white_player_row, white_player_col = current_row - 1, current_col
#             white_player_row, black_player_row = black_player_row, white_player_row
#             white_player_col, black_player_col = black_player_col, white_player_col
#             white_player, black_player = black_player, white_player
#     else:
#         if is_inside(current_row, current_col - 1, size) and matrix[current_row][current_col - 1] == white_pawn:
#             matrix[current_row][other_col] = black_pawn
#             position = (current_row, other_col)
#             is_capture = True
#             break
#         elif is_inside(current_row, current_col + 1, size) and matrix[current_row][current_col + 1] == white_pawn:
#             matrix[current_row][other_col] = black_pawn
#             position = (current_row, other_col)
#             is_capture = True
#             break
#         elif current_row == size - 1:
#             matrix[current_row][current_col] = black_pawn
#             position = (current_row, current_col)
#             is_queen = True
#             break
#         else:
#             matrix[current_row][current_col] = black_pawn
#             white_player_row, white_player_col = current_row + 1, current_col
#             white_player_row, black_player_row = black_player_row, white_player_row
#             white_player_col, black_player_col = black_player_col, white_player_col
#             white_player, black_player = black_player, white_player
#
#
# player = 'White' if white_player == 'w' else 'Black'
# (column_name, row_name) = get_chess_position(*position)
# position_name = f'{column_name}{row_name}'
#
# if is_capture:
#     print(f'Game over! {player} win, capture on {position_name}.')
#
# if is_queen:
#     print(f'Game over! {player} pawn is promoted to a queen at {position_name}.')
#
# for row in matrix:
#     print(*row, sep=" ")






def next_pos_white(row, col):
 return row - 1, col


def next_pos_black(row, col):
 return row + 1, col


size = 8
letter = {
 0: "a",
 1: "b",
 2: "c",
 3: "d",
 4: "e",
 5: "f",
 6: "g",
 7: "h"
}
white_pawn_row, white_pawn_col = 0, 0
black_pawn_row, black_pawn_col = 0, 0

matrix = []

for row in range(size):
 row_elements = input().split()
 for col in range(size):
  if row_elements[col] == "w":
   white_pawn_row, white_pawn_col = row, col
  elif row_elements[col] == "b":
   black_pawn_row, black_pawn_col = row, col
 matrix.append(row_elements)

is_captured = False
is_queen = False
turn = 0

while True:
 next_white_row, next_white_col = next_pos_white(white_pawn_row, white_pawn_col)
 white_pawn_row, white_pawn_col = next_white_row, next_white_col

 if abs(white_pawn_col - black_pawn_col) == 1 and white_pawn_row - black_pawn_row == 0:
  is_captured = True
  print(f"Game over! White win, capture on {letter[black_pawn_col]}{size - black_pawn_row}.")
  break

 if white_pawn_row == -1:
  is_queen = True
  print(f"Game over! White pawn is promoted to a queen at {letter[white_pawn_col]}8.")
  break

 next_black_row, next_black_col = next_pos_black(black_pawn_row, black_pawn_col)
 black_pawn_row, black_pawn_col = next_black_row, next_black_col

 if abs(white_pawn_col - black_pawn_col) == 1 and white_pawn_row - black_pawn_row == 0:
  is_captured = True
  print(f"Game over! Black win, capture on {letter[white_pawn_col]}{size - white_pawn_row}.")
  break

 if black_pawn_row == size:
  is_queen = True
  print(f"Game over! Black pawn is promoted to a queen at {letter[black_pawn_col]}1.")
  break