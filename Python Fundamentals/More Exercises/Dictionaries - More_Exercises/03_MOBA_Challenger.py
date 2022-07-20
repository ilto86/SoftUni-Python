# command = input()
# players = {}
# while command != "Season end":
#     args = command.split()
#     if args[1] == "->":
#         player = args[0]
#         position = args[2]
#         skill = int(args[4])
#
#         if player not in players:
#             players[player] = {position: skill}
#         else:
#             if position in players[player]:
#                 if players[player][position] < skill:
#                     players[player][position] = skill
#             else:
#                 players[player][position] = skill
#     else:
#         first_player = args[0]
#         second_player = args[2]
#         if first_player and second_player in players:
#             defeated = False
#             for key, value in players[first_player].items():
#                 for k, v in players[second_player].items():
#                     if key == k:
#                         if value > v:
#                             players.pop(second_player)
#                             defeated = True
#                             break
#                         elif value < v:
#                             players.pop(first_player)
#                             defeated = True
#                             break
#                 if defeated:
#                     break
#     command = input()
#
# players = dict(sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])))
# for key, inner_map in players.items():
#     print(f'{key}: {sum(inner_map.values())} skill')
#     inner_map = dict(sorted(inner_map.items(), key=lambda k: (-k[1], k[0])))
#
#     for key, value in inner_map.items():
#         print(f'- {key} <::> {value}')





# def register(players: dict, total_skill: dict, info: list):
#     if info[0] not in players.keys():
#         players[info[0]] = {}
#     if info[1] not in players[info[0]].keys():
#         players[info[0]][info[1]] = 0
#     if int(info[2]) > players[info[0]][info[1]]:
#         old_points = players[info[0]][info[1]]
#         players[info[0]][info[1]] = int(info[2])
#         if info[0] not in total_skill.keys():
#             total_skill[info[0]] = 0
#         else:
#             total_skill[info[0]] -= old_points
#         total_skill[info[0]] += int(info[2])
#
#
# def fight(players: dict, total_skill: dict, info: list):
#     if info[0] in total_skill.keys() and info[1] in total_skill.keys():
#         exists = False
#         for position in players[info[0]].keys():
#             if position in players[info[1]].keys():
#                 exists = True
#                 break
#         if exists:
#             if total_skill[info[0]] > total_skill[info[1]]:
#                 players.pop(info[1])
#                 total_skill.pop(info[1])
#             elif total_skill[info[0]] < total_skill[info[1]]:
#                 players.pop(info[0])
#                 total_skill.pop(info[0])
#
#
# players = {}
# total_skill = {}
# command = input()
# while not command == 'Season end':
#     if '->' in command:
#         command = command.split(' -> ')
#         register(players, total_skill, command)
#     else:
#         command = command.split(' vs ')
#         fight(players, total_skill, command)
#     command = input()
# total_skill = dict(sorted(total_skill.items(), key=lambda x: (-x[1], x[0])))
# for name in total_skill.keys():
#     print(f'{name}: {total_skill[name]} skill')
#     players[name] = dict(sorted(players[name].items(), key=lambda x: (-x[1], x[0])))
#     print(*[f'- {i} <::> {j}' for i, j in players[name].items()], sep='\n')





from collections import defaultdict


players = defaultdict(dict)

while True:
    data = input()
    if data == 'Season end':
        break
    if ' -> ' in data:
        player, position, skill = data.split(' -> ')
        skill = int(skill)
        new = True
        for p in players:
            if p == player:
                for ps, sk in players[p].items():
                    if ps == position:
                        new = False
                        if sk < skill:
                            players[player][position] = skill
        if new:
            players[player][position] = skill
    elif ' vs ' in data:
        player1, player2 = data.split(' vs ')
        found = False
        if player1 in players and player2 in players:
            for ps1, sk1 in players[player1].items():
                for ps2, sk2 in players[player2].items():
                    if ps1 == ps2:
                        found = True
                        player1_total = sum(players[player1].values())
                        player2_total = sum(players[player2].values())
                        if player1_total > player2_total:
                            players.pop(player2)
                        elif player1_total < player2_total:
                            players.pop(player1)
                    if found:
                        break
                if found:
                    break

for player in sorted(players, key=lambda p: -sum(players[p].values())):
    total = sum(players[player].values())
    print(f'{player}: {total} skill')
    for position, skill in sorted(players[player].items(), key=lambda x: (-x[1], x[0])):
        print(f'- {position} <::> {skill}')