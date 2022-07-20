matrix = [['-', '-', '-'],
          ['-', '-', '-'],
          ['-', '-', '-']]

print(f'Please enter first player username:')
first_player = input()
print(f'Please enter second player username:')
second_player = input()

for row_index in range(len(matrix)):
    print(*matrix[row_index])

moves_counter = 0
winner = ''

while True:
    if moves_counter % 2 == 0:
        print(f'{first_player} turn, please put coordinates for example: 0, 0 on next line put a X sign')
    else:
        print(f'{second_player} turn, please put coordinates for example: 0, 0 on next line put a O sign')
    row, col = [int(el) for el in input().split(", ")]
    sign = input()
    matrix[row][col] = sign
    for row_index in range(len(matrix)):
        print(*matrix[row_index])
    moves_counter += 1
    if matrix[0].count('X') == 3 or matrix[1].count('X') == 3 or matrix[2].count('X') == 3:
        winner = first_player
        break
    elif matrix[0].count('O') == 3 or matrix[1].count('O') == 3 or matrix[2].count('O') == 3:
        winner = second_player
        break
    elif (matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X') \
            or matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X':
        winner = first_player
        break
    elif matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == '0' \
            or matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O':
        winner = second_player
        break
    elif (matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X') \
            or (matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X') \
            or (matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X'):
        winner = first_player
        break
    elif (matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O') \
            or (matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O') \
            or (matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O'):
        winner = second_player
        break
    if moves_counter == 9:
        break

if moves_counter == 9:
    print('No winner')
else:
    print(f'Winner is {winner}')