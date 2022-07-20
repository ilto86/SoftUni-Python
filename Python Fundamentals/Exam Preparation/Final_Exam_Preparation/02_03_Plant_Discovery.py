# numbers_of_plants = int(input())
# discovered_plants = {}
#
# for plant in range(numbers_of_plants):
#     plant_name, rarity = input().split("<->")
#     if plant_name not in discovered_plants:
#         discovered_plants[plant_name] = {"rarity": int(rarity), "rating": []}
#
# command = input()
# while command != "Exhibition":
#     action, value = command.split(": ")
#
#     if action == "Rate":
#         plant, new_rating = value.split(" - ")
#         if plant in discovered_plants:
#             discovered_plants[plant]["rating"].append(int(new_rating))
#         else:
#             print("error")
#
#     elif action == "Update":
#         plant, new_rarity = value.split(" - ")
#         if plant in discovered_plants:
#             discovered_plants[plant]["rarity"] = int(new_rarity)
#         else:
#             print("error")
#
#     elif action == "Reset":
#         plant = value
#         if plant in discovered_plants:
#             discovered_plants[plant]["rating"].clear()
#         else:
#             print("error")
#
#     command = input()
#
# for plant, plants_value in discovered_plants.items():
#     if discovered_plants[plant]['rating']:
#         discovered_plants[plant]['average'] = sum(discovered_plants[plant]['rating'])/len(discovered_plants[plant]['rating'])
#     else:
#         discovered_plants[plant]['average'] = 0
#
# print("Plants for the exhibition:")
#
# for plant_name, value in discovered_plants.items():
#     print(f"- {plant_name}; Rarity: {value['rarity']}; Rating: {value['average']:.2f}")






# n = int(input())
# plants = {}
#
#
# for _ in range(n):
#     plant, rarity = input().split('<->')
#     plants[plant] = {'rarity': int(rarity), 'ratings': []}
#
# data = input()
#
# while not data == "Exhibition":
#     command, value = data.split(': ')
#     try:
#         if command == "Rate":
#             plant, rating = value.split(" - ")
#             plants[plant]['ratings'].append(int(rating))
#         elif command == "Update":
#             plant, rarity = value.split(" - ")
#             plants[plant]['rarity'] = int(rarity)
#         elif command == "Reset":
#             plant = value
#             plants[plant]['ratings'].clear()
#     except:
#         print("error")
#     data = input()
#
# for plant_name, plants_data in plants.items():
#     if plants[plant_name]['ratings']:
#         plants[plant_name]['avg'] = sum(plants[plant_name]['ratings'])/len(plants[plant_name]['ratings'])
#     else:
#         plants[plant_name]['avg'] = 0
#
# sorted_plants = sorted(plants.items(), key=lambda x: (x[1]['rarity'], x[1]['avg']), reverse=True)
#
# print("Plants for the exhibition:")
# for plant_name, value in sorted_plants:
#     print(f"- {plant_name}; Rarity: {value['rarity']}; Rating: {value['avg']:.2f}")







# iterations = int(input())
#
# flower_colection = {}
# for discovored_flowers in range (iterations):
#     plants = input().split("<->")
#     plant = plants[0]
#     rarity = int(plants[1])
#     rating = 0
#     if plant not in flower_colection:
#         flower_colection[plant] = []
#     flower_colection[plant].append(rarity)
#     flower_colection[plant].append(rating)
#
# plant_rating = {}
# command = input()
# while not command == "Exhibition":
#     command = command.split((": "))
#     action = command[0]
#
#     if action == "Rate":
#         plant, rating = command[1].split(" - ")
#         rating = int(rating)
#         if plant not in flower_colection:
#             print("error")
#         else:
#             if plant not in plant_rating:
#                 plant_rating[plant] = []
#             plant_rating[plant].append(rating)
#
#     elif action == "Update":
#         plant, new_rarity = command[1].split(" - ")
#         new_rarity = int(new_rarity)
#         if plant not in flower_colection:
#             print("error")
#         else:
#             flower_colection[plant][0] = new_rarity
#
#     else:
#         plant = command[1]
#         if plant not in flower_colection:
#             print("error")
#         else:
#             plant_rating[plant].clear()
#
#     command = input()
# for key, value in plant_rating.items():
#     if sum(value) == 0:
#        value = 0
#        # plant_rating[key] = value
#     else:
#         value = sum(value) / len(value)
#         plant_rating[key] = value
#     for plants, rarity in flower_colection.items():
#         if plants == key:
#             flower_colection[key][1] = value
#
# # flower_colection = dict(sorted(flower_colection.items(), key= lambda x: ( -x[1][0], -x[1][1] )))
# print("Plants for the exhibition:")
# for key, value in flower_colection.items():
#
#     print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")








# numbers_of_plants = int(input())
# discovered_plants = {}
# for plant in range(numbers_of_plants):
#     data = input().split("<->")
#     plant_name = data[0]
#     rarity = int(data[1])
#     rating = []
#     if plant_name not in discovered_plants:
#         discovered_plants[plant_name] = {"rarity": rarity, "rating": rating}
#
#
# while True:
#     commands = input()
#
#     if commands == "Exhibition":
#         break
#
#     command = commands.split(": ")
#     if command[0] == "Rate":
#         some_command = command[1].split(" - ")
#         plant = some_command[0]
#         new_rating = float(some_command[1])
#         if plant in discovered_plants:
#             discovered_plants[plant]["rating"].append(new_rating)
#         else:
#             print("error")
#
#     elif command[0] == "Update":
#         some_command = command[1].split(" - ")
#         plant = some_command[0]
#         new_rarity = int(some_command[1])
#         if plant in discovered_plants:
#             discovered_plants[plant]["rarity"] = new_rarity
#         else:
#             print("error")
#
#     elif command[0] == "Reset":
#         plant = command[1]
#         if plant in discovered_plants:
#             discovered_plants[plant]["rating"].clear()
#         else:
#             print("error")
#
# print("Plants for the exhibition:")
# for key, value in discovered_plants.items():
#     print(f"- {key}", end='; ')
#     for k, v in value.items():
#         if k == "rarity":
#             print(f"Rarity: {v}", end='; ')
#         elif k == "rating":
#             if len(v) > 0:
#                 average_rating = sum(v) / len(v)
#                 print(f"Rating: {average_rating:.2f}")
#             else:
#                 average_rating = 0
#                 print(f"Rating: {average_rating:.2f}")




numbers_of_plants = int(input())
plants = {}

for n in range(numbers_of_plants):
    data = input().split("<->")
    plant, rarity = data[0], int(data[1])
    plants[plant] = {"rarity": rarity, "rating":[]}

while True:
    data = input()
    if data == "Exhibition":
        break
    commands = data.split(": ")
    command = commands[0]
    new_data = commands[1].split(" - ")

    if command == "Rate":
        plant = new_data[0]
        rating = int(new_data[1])
        if plant not in plants:
            print("error")
        else:
            plants[plant]["rating"].append(rating)

    elif command == "Update":
        plant = new_data[0]
        new_rarity = int(new_data[1])
        if plant not in plants:
            print("error")
        else:
            plants[plant]["rarity"] = new_rarity
    elif command == "Reset":
        plant = new_data[0]
        if plant not in plants:
            print("error")
        else:
            plants[plant]["rating"].clear()

print("Plants for the exhibition: ")

for plant, plants_value in plants.items():
    if plants[plant]['rating']:
        plants[plant]['average'] = sum(plants[plant]['rating']) / len(plants[plant]['rating'])
    else:
        plants[plant]['average'] = 0

for key, value in plants.items():
    plant_name = key
    rarity = value["rarity"]
    average_rating = value["average"]
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")