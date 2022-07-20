# command_line1 = input()
# cities = {}
# # Havana -> Population: 410000 citizens, Gold: 1100 kg
# while command_line1 != "Sail":
#     args = command_line1.split("||")
#     city = args[0]
#     population = int(args[1])
#     gold = int(args[2])
#
#     if city not in cities:
#         cities[city] = {"population": 0, "gold": 0}
#     cities[city]["population"] += population
#     cities[city]["gold"] += gold
#     command_line1 = input()
#
# command_line2 = input()
# while command_line2 != "End":
#     args = command_line2.split("=>")
#     command = args[0]
#     city = args[1]
#     if command == "Plunder":
#         people = int(args[2])
#         gold = int(args[3])
#         cities[city]["population"] -= people
#         cities[city]["gold"] -= gold
#         print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')
#
#         if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
#             print(f'{city} has been wiped off the map!')
#             del cities[city]
#     elif command == "Prosper":
#         gold = int(args[2])
#         if gold < 0:
#             print(f'Gold added cannot be a negative number!')
#         else:
#             cities[city]["gold"] += gold
#             print(f'{gold} gold added to the city treasury. {city} now has {cities[city]["gold"]} gold.')
#     command_line2 = input()
#
# print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
# cities = dict(sorted(cities.items(), key=lambda y: (-y[1]['gold'], y[0])))
#
# for key, value in cities.items():
#     print(f'{key} -> Population: {value["population"]} citizens, Gold: {value["gold"]} kg')





# target_cities_dict = {}
#
# while True:
#
#     command = input()
#
#     if command == "Sail":
#         break
#     token = command.split("||")
#     town = token[0]
#     population = int(token[1])
#     gold = int(token[2])
#
#     if town not in target_cities_dict:
#         target_cities_dict[town] = [population, gold]
#     else:
#         target_cities_dict[town][0] += population
#         target_cities_dict[town][1] += gold
#
# while True:
#
#     command = input()
#
#     if command == "End":
#         break
#
#     token = command.split("=>")
#
#     if token[0] == "Plunder":
#         town = token[1]
#         people = int(token[2])
#         gold = int(token[3])
#
#         print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
#         target_cities_dict[town][0] -= people
#         target_cities_dict[town][1] -= gold
#
#         if target_cities_dict[town][0] <= 0 or target_cities_dict[town][1] <= 0:
#             print(f"{town} has been wiped off the map!")
#             del target_cities_dict[town]
#
#     elif token[0] == "Prosper":
#         town = token[1]
#         gold = int(token[2])
#
#         if gold < 0:
#             print(f"Gold added cannot be a negative number!")
#             continue
#         else:
#             target_cities_dict[town][1] += gold
#             print(f"{gold} gold added to the city treasury. {town} now has {target_cities_dict[town][1]} gold.")
#
# sorted_dict = dict(sorted(target_cities_dict.items(), key=lambda x: (- x[1][1], x[0])))
#
# if len(target_cities_dict) > 0:
#     print(f"Ahoy, Captain! There are {len(target_cities_dict)} wealthy settlements to go to:")
#
#     for key, val in sorted_dict.items():
#         print(f"{key} ->", end= ' ')
#         print(f"Population: {val[0]} citizens, Gold: {val[1]} kg")
#
# else:
#     print(f"Ahoy, Captain! All targets have been plundered and destroyed!")





# target_log = {}
#
# while True:
#     args = input()
#     if args == 'Sail':
#         break
#     args = args.split('||')
#     town = args[0]
#     population = int(args[1])
#     gold = int(args[2])
#     if town not in target_log:
#         target_log[town] = [population, gold]
#     else:
#         target_log[town][0] += population
#         target_log[town][1] += gold
#
# while True:
#     tokens = input()
#     if tokens == 'End':
#         break
#     tokens = tokens.split('=>')
#     command = tokens[0]
#     city = tokens[1]
#     if command == 'Plunder':
#         people = int(tokens[2])
#         money = int(tokens[3])
#         if city in target_log:
#             target_log[city][0] -= people
#             target_log[city][1] -= money
#             print(f'{city} plundered! {money} gold stolen, {people} citizens killed.')
#             if target_log[city][0] <= 0 or target_log[city][1] <= 0:
#                 print(f'{city} has been wiped off the map!')
#                 target_log.pop(city)
#
#     elif command == 'Prosper':
#         money = int(tokens[2])
#         if money > 0:
#             target_log[city][1] += money
#             print(f'{money} gold added to the city treasury. {city} now has {target_log[city][1]} gold.')
#         elif money < 0:
#             print(f'Gold added cannot be a negative number!')
#
# sorted_target_log = dict(sorted(target_log.items(), key=lambda x: (-x[1][1], x[0])))
#
# if len(sorted_target_log) > 0:
#     print(f'Ahoy, Captain! There are {len(sorted_target_log)} wealthy settlements to go to:')
#     for k,v in sorted_target_log.items():
#         print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg')
# else:
#     print('Ahoy, Captain! All targets have been plundered and destroyed!')








# def extract_func(command, data_dict):
#     command = command.split('||')
#     town = command[0]
#     population = int(command[1])
#     gold = int(command[2])
#
#     if town not in data_dict:
#         data_dict[town] = [population, gold]
#     else:
#         data_dict[town][0] += population
#         data_dict[town][1] += gold
#
#     return data_dict
#
#
# def sail_func(command, data_dict):
#     command = command.split('=>')
#     current_command = command[0]
#
#     if current_command == 'Plunder':
#         town = command[1]
#         people = int(command[2])
#         gold = int(command[3])
#
#         data_dict[town][0] -= people
#         data_dict[town][1] -= gold
#
#         print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
#
#         if data_dict[town][0] <= 0 or data_dict[town][1] <= 0:
#             del data_dict[town]
#             print(f"{town} has been wiped off the map!")
#
#     elif current_command == 'Prosper':
#         town = command[1]
#         gold = int(command[2])
#
#         if gold > 0:
#             data_dict[town][1] += gold
#             print(f"{gold} gold added to the city treasury. {town} now has {data_dict[town][1]} gold.")
#         else:
#             print("Gold added cannot be a negative number!")
#
#     return data_dict
#
#
# def pirates():
#     data_dict = {}
#     condition = False
#     while True:
#         command = input()
#
#         if command == 'End':
#             break
#         elif command != 'Sail' and not condition:
#             data_dict = extract_func(command, data_dict)
#
#         elif command == 'Sail':
#             condition = True
#             continue
#
#         elif condition:
#             data_dict = sail_func(command, data_dict)
#
#     print(f'Ahoy, Captain! There are {len(data_dict)} wealthy settlements to go to:')
#
#     for data in data_dict:
#         town = data
#         current_population = data_dict[data][0]
#         current_gold = data_dict[data][1]
#         print(f'{town} -> Population: {current_population} citizens, Gold: {current_gold} kg')
#
#
# pirates()



# cities = {}
#
# while True:
#     text = input()
#     if text == "Sail":
#         break
#
#     data = text.split("||")
#     city = data[0]
#     population = int(data[1])
#     gold = int(data[2])
#     if city not in cities:
#         cities[city] = [population, gold]
#     else:
#         cities[city][0] += population
#         cities[city][1] += gold
#
#
# while True:
#     text = input()
#     if text == "End":
#         break
#     data = text.split("=>")
#     command = data[0]
#     town = data[1]
#
#     if command == "Plunder":
#         people = int(data[2])
#         gold = int(data[3])
#         cities[town][0] -= people
#         cities[town][1] -= gold
#         print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
#         if cities[town][0] <= 0 or cities[town][1] <= 0:
#             print(f"{town} has been wiped off the map!")
#             del cities[town]
#     elif command == "Prosper":
#         gold = int(data[2])
#         if gold < 0:
#             print(f"Gold added cannot be a negative number!")
#         else:
#             cities[town][1] += gold
#             print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
#
# if cities:
#     print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
#     for key, value in cities.items():
#         print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")


cities = {}

while True:
    string = input()

    if string == "Sail":
        break

    data = string.split("||")

    city, population, gold = data[0], int(data[1]), int(data[2])
    if city not in cities:
        cities[city] = {'Population': population, 'Gold': gold}
    else:
        cities[city]['Population'] += population
        cities[city]['Gold'] += gold

while True:
    data = input()

    if data == "End":
        break

    commands = data.split("=>")
    command = commands[0]
    town = commands[1]

    if command == "Plunder":
        people = int(commands[2])
        gold = int(commands[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]['Population'] -= people
        cities[town]['Gold'] -= gold
        if cities[town]['Population'] == 0 or cities[town]['Gold'] == 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]

    elif command == "Prosper":
        gold = int(commands[2])
        if gold <= 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]['Gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['Gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

    for city, treasure in cities.items():
        people = treasure['Population']
        gold = treasure['Gold']
        print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")