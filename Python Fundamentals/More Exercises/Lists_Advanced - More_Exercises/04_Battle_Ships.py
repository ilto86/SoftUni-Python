# def create_field(n):
#     result = []
#     for line in range(n):
#         result.append([int(el) for el in input().split()]) # turn elements into ints
#     return result
#
# def is_ship(field, row, col):
#     if field[row][col] > 0:
#         return True
#
# def attack_cell(field, row, col, destroyed_ships):
#     if field[row][col] > 1:
#         field[row][col] -= 1
#     else:
#         field[row][col] = 0
#         destroyed_ships += 1
#     return destroyed_ships
#
# def execute_attacks(attacks_info, field):
#     destroyed_ships = 0
#
#     for attack in attacks_info:
#         row = int(attack[0])
#         column = int(attack[2])
#         if is_ship(field, row, column):
#             destroyed_ships = attack_cell(field, row, column, destroyed_ships)
#
#     return destroyed_ships
#
# n = int(input())
# field = create_field(n)
# attacks = input().split()
# ships_destroyed = execute_attacks(attacks, field)
# print(ships_destroyed)





n = int(input())
ships_list = []
destroyed_ships = 0
for _ in range(n):
    ships_list.append(list(map(lambda x: int(x), input().split())))
attacks_list = input().split()
for i in attacks_list:
    attack = i.split('-')
    row = int(attack[0])
    place = int(attack[1])
    if ships_list[row][place] > 0:
        ships_list[row][place] -= 1
        if ships_list[row][place] == 0:
            destroyed_ships += 1
print(destroyed_ships)

