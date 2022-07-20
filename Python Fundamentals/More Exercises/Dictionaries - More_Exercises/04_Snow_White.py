command = input()
dwarfs = {}
hats = {}

while command != "Once upon a time":
    name = command.split(" <:> ")[0]
    color = command.split(" <:> ")[1]
    physics = int(command.split(" <:> ")[2])


    element = f'({color}) {name}'
    if element not in dwarfs.keys():
        dwarfs[element] = [color, 0]
        if color not in hats.keys():
            hats[color] = 0
        hats[color] += 1
    if physics > dwarfs[element][1]:
        dwarfs[element][1] = physics

    command = input()

inner_map = sorted(dwarfs.items(), key=lambda x: (-x[1][1], -hats[x[1][0]]))
for key, value in inner_map:
    print(f"{key} <-> {value[1]}")





# def register(name: str, hat_colour: str, points: int, dwarfs: dict, hats: dict):
#     element = f'({hat_colour}) {name}'
#     if element not in dwarfs.keys():
#         dwarfs[element] = [hat_colour, 0]
#         if hat_colour not in hats.keys():
#             hats[hat_colour] = 0
#         hats[hat_colour] += 1
#     if points > dwarfs[element][1]:
#         dwarfs[element][1] = points
#
#
# dwarfs_dict = {}
# hats_dict = {}
#
# command = input()
# while not command == 'Once upon a time':
#     command = command.split(' <:> ')
#     register(command[0], command[1], int(command[2]), dwarfs_dict, hats_dict)
#
#     command = input()
#
# result = sorted(dwarfs_dict.items(), key=lambda x: (-x[1][1], -hats_dict[x[1][0]]))
# for i, j in result:
#     print(f"{i} <-> {j[1]}")


# result = {i: j for i, j in sorted(dwarfs_dict.items(), key=lambda x: (-x[1][1], -hats_dict[x[1][0]]))}
# [print(f'{i} <-> {j[1]}') for i, j in result.items()]