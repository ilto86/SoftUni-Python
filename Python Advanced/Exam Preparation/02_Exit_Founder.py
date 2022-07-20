# player_1, player_2 = input().split(", ")
#
# size = 6
# board = []
# exit_win_position = []
# trap_game_ends = []
#
# for row in range(size):
#     row_elements = [x for x in input().split()]
#     for col in range(size):
#         if row_elements[col] == "E":
#             exit_win_position.append(row)
#             exit_win_position.append(col)
#
#     board.append(row_elements)
#
# counter_ignor_tom = False
# ignored_tom = "Tom"
# counter_ignor_jerry = False
# ignored_jerry = "Jerry"
# while True:
#     current_player, other_player = player_1, player_2
#     player_row, player_col = [int(x) for x in input()[1:-1].split(', ')]
#
#     if counter_ignor_tom and current_player == ignored_tom:
#             counter_ignor_tom = False
#             player_1, player_2 = player_2, player_1
#             continue
#     if counter_ignor_jerry and current_player == ignored_jerry:
#         counter_ignor_jerry = False
#         player_1, player_2 = player_2, player_1
#         continue
#
#     if board[player_row][player_col] == "E":
#         print(f"{current_player} found the Exit and wins the game!")
#         break
#     elif board[player_row][player_col] == "T":
#         print(f"{current_player} is out of the game! The winner is {other_player}.")
#         break
#     elif board[player_row][player_col] == "W":
#         print(f"{current_player} hits a wall and needs to rest.")
#         if current_player == ignored_tom:
#             counter_ignor_tom = True
#             player_1, player_2 = player_2, player_1
#         else:
#             counter_ignor_jerry = True
#             player_1, player_2 = player_2, player_1
#     else:
#         player_1, player_2 = player_2, player_1



player_1, player_2 = input().split(', ')

matrix = [[x for x in input().split()] for _ in range(6)]

counter = 0

player_to_rest = []

while True:

    row, col = [int(x) for x in input() if x.isdigit()]
    player = player_1 if counter % 2 == 0 else player_2

    if player_to_rest and player_to_rest[0] == player:
        del player_to_rest[0]

    elif matrix[row][col] == 'E':
        print(f'{player} found the Exit and wins the game!')
        break
    elif matrix[row][col] == 'T':
        winner = player_1 if player == player_2 else player_2
        print(f'{player} is out of the game! The winner is {winner}.')
        break
    elif matrix[row][col] == 'W':
        print(f'{player} hits a wall and needs to rest.')
        player_to_rest.append(player)

    counter += 1