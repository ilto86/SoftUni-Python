# queue = input()
#
# animals = queue.split(', ')
# ship_counter = 0
#
# for position, animal in enumerate(reversed(animals)):
#     if position == 0 and animal == 'wolf':
#         print('Please go away and stop eating my sheep')
#         break
#     elif position != 0 and animal == 'wolf':
#         print(f'Oi! Sheep number {ship_counter}! You are about to be eaten by a wolf!')
#         break
#     else:
#         ship_counter += 1

# animals = input()
#
# animals_list = animals.split(sep=', ')
#
# if animals_list[-1] == 'wolf':
#     print('Please go away and stop eating my sheep')
# else:
#     for idx, animal in enumerate(animals_list):
#         if animal == 'wolf':
#             print(
#                 f'Oi! Sheep number {len(animals_list)-idx-1}! You are about to be eaten by a wolf!')
#             break

animals = input().split(", ")

for animal_index in range(len(animals)):
    if animals[animal_index] == "wolf":
        if animals[animal_index] == animals[-1]:
            print("Please go away and stop eating my sheep")
        else:
            sheep_num = len(animals[animal_index+1:])
            print(f"Oi! Sheep number {sheep_num}! You are about to be eaten by a wolf!")