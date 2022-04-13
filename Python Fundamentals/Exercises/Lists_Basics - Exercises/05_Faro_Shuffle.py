cards = input().split()
n = int(input())

half_size = len(cards) // 2 # half_size = int(len(cards)) / 2

for shuffle in range(n):
    left_side = cards[0:half_size]
    right_side = cards[half_size:]

    faro_cards = []

    for index in range(len(left_side)):
        faro_cards.append(left_side[index])
        faro_cards.append(right_side[index])

    cards = faro_cards

print(cards)


# card_deck = input().split()
# number_of_shuffles = int(input())
# final_deck = []
# for shuffle in range(number_of_shuffles):
#     final_deck = []
#     middle_of_the_deck = len(card_deck) // 2 # int(len(card_deck) / 2)
#     left_half = card_deck[:middle_of_the_deck]
#     right_half = card_deck[middle_of_the_deck:]
#     for index_of_the_card in range(len(left_half)):
#         final_deck.append(left_half[index_of_the_card])
#         final_deck.append(right_half[index_of_the_card])
#     card_deck = final_deck
# print(card_deck)



# cards = input()
# number_of_shuffle = int(input())
# cards_list = cards.split(" ")  # Превръщаме стринга в лист
# center_card = int(len(cards_list) / 2)  # Взимаме половината от броя елементи в листа за двете половини на тестето
#
# for i in range(number_of_shuffle):  # Лупваме през броя размесвания
#     cards_list_copy = cards_list.copy()  # Копираме листа в друг лист за да можем да изтрием първоначалния
#     cards_list.clear()  # Изчистваме първоначалния лист
#     for j in range(center_card):  # Лупваме през средата на листа за да може да вземем
#         # по една карта от двете половини на тестето
#         cards_list.append(cards_list_copy[j])
#         cards_list.append(cards_list_copy[j + center_card])
#
# print(cards_list)


# string = input().split(' ')
# shuffle = int(input())
# shuffled = []
#
# for i in range(shuffle):
#     half1 = string[:len(string) // 2]
#     half2 = string[len(string) // 2:]
#
#     for j in zip(half1, half2):
#         shuffled.extend(j)
#     string = shuffled
#     shuffled = []
#
# print(string)