def doubled(row, col, board):
    number_sum =  board[row][0] + board[row][6] +  board[0][col] + board[6][col]
    result = number_sum * 2
    return result


def tripled(row, col, board):
    number_sum = board[row][0] + board[row][6] + board[0][col] + board[6][col]
    result = number_sum * 3
    return result


player_one, player_two = input().split(", ")
dart_size = 7
dartboard = [[int(x) if x.isdigit() else x for x in input().split()] for x in range(dart_size)]
player_one_score = 501
player_two_score = 501
player_one_throw = 0
player_two_throw = 0
player_count = 0

while True:
    player = player_one
    throw_row, throw_col = [int(x) for x in input()[1:-1].split(', ')]
    # throw_row, throw_col = [int(x) for x in input().strip('(').strip(')').split(', ')]
    # action = input().split(", ")
    # action_row = action[0].strip().split("(")
    # action_col = action[1].strip().split(")")
    # throw_row = int(action_row[1])
    # throw_col = int(action_col[0])
    player_one_throw += 1
    player_count = player_one_throw

    if throw_row < 0 or throw_col < 0 or throw_row >= dart_size or throw_col >= dart_size:
        player_one, player_two = player_two, player_one
        player_one_score, player_two_score = player_two_score, player_one_score
        player_one_throw, player_two_throw = player_two_throw, player_one_throw
        continue

    if dartboard[throw_row][throw_col] == "B":
        print(f"{player} won the game with {player_count} throws!")
        break

    if dartboard[throw_row][throw_col] == "D":
        player_one_score -= doubled(throw_row, throw_col, dartboard)

    if dartboard[throw_row][throw_col] == "T":
        player_one_score -= tripled(throw_row, throw_col, dartboard)

    if dartboard[throw_row][throw_col] != "D" and dartboard[throw_row][throw_col] != "T":
        player_one_score -= dartboard[throw_row][throw_col]

    if player_one_score <= 0:
        print(f"{player} won the game with {player_count} throws!")
        break

    player_one, player_two = player_two, player_one
    player_one_score, player_two_score = player_two_score, player_one_score
    player_one_throw, player_two_throw = player_two_throw, player_one_throw