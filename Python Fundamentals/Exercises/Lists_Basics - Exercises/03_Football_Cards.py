# red_card = input().split(" ")
# team_a = ["A-1","A-2","A-3","A-4","A-5","A-6","A-7","A-8","A-9","A-10","A-11"]
# team_b = ["B-1","B-2","B-3","B-4","B-5","B-6","B-7","B-8","B-9","B-10","B-11"]
# sequence_of_cards = red_card
# players_count_a = 11
# players_count_b = 11
# terminated = False
#
# for cards in sequence_of_cards:
#     if "A" in cards:
#         if cards not in team_a:
#             continue
#         team_a.remove(cards)
#         players_count_a -= 1
#
#     if "B" in cards:
#         if cards not in team_b:
#             continue
#         team_b.remove(cards)
#         players_count_b -= 1
#     if len(team_a) < 7 or len(team_b) < 7:
#         terminated = True
#         break
#
# print(f"Team A - {players_count_a}; Team B - {players_count_b}")
# if terminated:
#     print("Game was terminated")



# team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
#
# red_card = input()
# sequence_of_cards = red_card.split(" ")
#
# game_terminated = False
#
# for cards in sequence_of_cards:
#     if "A" in cards:
#         if cards not in team_a:
#             continue
#         team_a.remove(cards)
#
#     elif "B" in cards:
#         if cards not in team_b:
#             continue
#         team_b.remove(cards)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_terminated = True
#         break
#
# if game_terminated:
#     print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#     print("Game was terminated")
# else:
#     print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")




# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
#
# game_is_terminated = False
#
# sent_off_players = input()
# sent_off_players_list = sent_off_players.split(" ")
# for player in sent_off_players_list:
#     if 'A' in player:
#         if player not in team_a:
#             continue
#         team_a.remove(player)
#     elif 'B' in player:
#         if player not in team_b:
#             continue
#         team_b.remove(player)
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_is_terminated = True
#         break
#
# if game_is_terminated:
#     print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#     print("Game was terminated")
# else:
#     print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")


# team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# cards_input = input().split()
# terminated = False
#
# for card in cards_input:            # for i in range(len(cards_input)):
#     card_info = card.split('-')     # card_info = cards_input[i]
#
#     team_name = card_info[0]
#     player_number = int(card_info[1])
#
#     if team_name == 'A' and player_number in team_a:
#         team_a.remove(player_number)
#     elif team_name == 'B' and player_number in team_b:
#         team_b.remove(player_number)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         terminated = True
#         break
#
# print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
# if terminated:
#     print('Game was terminated')



# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# game_was_terminated = False
# sent_off_players = input().split(" ")
#
# for player in sent_off_players:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_was_terminated = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if game_was_terminated:
#     print("Game was terminated")



# team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# cards_input = input().split()
# terminated = False
#
# for card in cards_input:            # for i in range(len(cards_input)):
#     card_info = card.split('-')     # card_info = cards_input[i]
#
#     team_name = card_info[0]
#     player_number = int(card_info[1])
#
#     if team_name == 'A' and player_number in team_a:
#         team_a.remove(player_number)
#     elif team_name == 'B' and player_number in team_b:
#         team_b.remove(player_number)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         terminated = True
#         break
#
# print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
# if terminated:
#     print('Game was terminated')

# info = input().split(" ")
# team_a_players = 11
# team_b_players = 11
# players_loses = []
# condition = False
#
# for card in info:
#     if card not in players_loses:
#         players_loses.append(card)
#         if "A" in card:
#             team_a_players -= 1
#
#         elif "B" in card:
#             team_b_players -= 1
#
#         if team_a_players < 7 or team_b_players < 7:
#             condition = True
#             break
#
# print(f"Team A - {team_a_players}; Team B - {team_b_players}")
# if condition:
#     print("Game was terminated")



cards = input().split(" ")
team_a_players = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b_players = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
condition = False

for card in cards:
        if "A" in card and card in team_a_players:
            team_a_players.remove(card)

        elif "B" in card and card in team_b_players:
            team_b_players.remove(card)

        if len(team_a_players) < 7 or len(team_b_players) < 7:
            condition = True
            break

print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
if condition:
    print("Game was terminated")