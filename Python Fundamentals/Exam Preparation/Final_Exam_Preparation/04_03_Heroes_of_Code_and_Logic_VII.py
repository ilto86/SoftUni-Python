# count = int(input())
# heroes = dict()
#
#
# for i in range(count):
#     current_hero = input().split()
#     hero_name = current_hero[0]
#     hero_HP = int(current_hero[1])
#     hero_MP = int(current_hero[2])
#
#     current_hero_dict = dict()
#     current_hero_dict["HP"] = hero_HP
#     current_hero_dict["MP"] = hero_MP
#     heroes[hero_name] = current_hero_dict
#
# command = input()
#
# while command != "End":
#     command_params = command.split(" - ")
#     command_name = command_params[0]
#     hero_name = command_params[1]
#     value = int(command_params[2])
#
#     if command_name == "Heal":
#         if heroes[hero_name]["HP"] +  value > 100:
#             value = 100 - heroes[hero_name]["HP"]
#             heroes[hero_name]["HP"] = 100
#         else:
#             heroes[hero_name]["HP"] += value
#
#         print(f"{hero_name} healed for {value} HP!")
#
#     elif command_name == "Recharge":
#         if heroes[hero_name]["MP"] + value > 200:
#             value = 200 - heroes[hero_name]["MP"]
#             heroes[hero_name]["MP"] = 200
#         else:
#             heroes[hero_name]["MP"] += value
#
#         print(f"{hero_name} recharged for {value} MP!")
#
#     elif command_name == "TakeDamage":
#         attacker = command_params[3]
#         heroes[hero_name]["HP"] -= value
#         if heroes[hero_name]["HP"] > 0:
#             print(f"{hero_name} was hit for {value} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
#         else:
#             heroes.pop(hero_name)
#             print(f"{hero_name} has been killed by {attacker}!")
#
#     elif command_name == "CastSpell":
#         spell = command_params[3]
#         if heroes[hero_name]["MP"] >= value:
#             heroes[hero_name]["MP"] -= value
#             print(f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name]['MP']} MP!")
#         else:
#             print(f"{hero_name} does not have enough MP to cast {spell}!")
#
#     command = input()
#
# for hero in heroes:
#     print(f"{hero}")
#     print(f" HP: {heroes[hero]['HP']}")
#     print(f" MP: {heroes[hero]['MP']}")






# count = int(input())
# heroes = {}
#
# for _ in range(count):
#     hero, hp, mp = input().split()
#     heroes[hero] = {"HP": int(hp), "MP": int(mp)}
#
# while True:
#     data = input()
#
#     if data == "End":
#         break
#
#     commands = data.split(" - ")
#     command = commands[0]
#     hero_name = commands[1]
#
#     if command == "CastSpell":
#         needed_MP = int(commands[2])
#         spell_name = commands[3]
#         if needed_MP <= heroes[hero_name]["MP"]:
#             heroes[hero_name]["MP"] -= needed_MP
#             print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
#         else:
#             print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#
#     if command == "TakeDamage":
#         damage = int(commands[2])
#         attacker = commands[3]
#         heroes[hero_name]["HP"] -= damage
#         if heroes[hero_name]["HP"] <= 0:
#             del heroes[hero_name]
#             print(f"{hero_name} has been killed by {attacker}!")
#         else:
#             print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
#
#     if command == "Recharge":
#         amount_mp = int(commands[2])
#         if heroes[hero_name]["MP"] + amount_mp < 200:
#             heroes[hero_name]["MP"] += amount_mp
#         else:
#             amount_mp = 200 - heroes[hero_name]["MP"]
#             heroes[hero_name]["MP"] = 200
#         print(f"{hero_name} recharged for {amount_mp} MP!")
#
#     if command == "Heal":
#         amount_hp = int(commands[2])
#         if heroes[hero_name]["HP"] + amount_hp < 100:
#             heroes[hero_name]["HP"] += amount_hp
#         else:
#             amount_hp = 100 - heroes[hero_name]["HP"]
#             heroes[hero_name]["HP"] = 100
#         print(f"{hero_name} healed for {amount_hp} HP!")
#
# for hero in heroes:
#     print(hero)
#     print(f"  HP: {heroes[hero]['HP']}")
#     print(f"  MP: {heroes[hero]['MP']}")





number_of_heroes = int(input())
heroes = {}

for _ in range(number_of_heroes):
    data = input().split()
    hero = data[0]
    hp = int(data[1])
    mp = int(data[2])
    heroes[hero] = {"HP": hp, "MP": mp}

while True:
    data = input()

    if data == "End":
        break
    commands = data.split(" - ")
    command = commands[0]
    hero_name = commands[1]

    if command == "CastSpell":
        mp_needed = int(commands[2])
        spell_name = commands[3]
        if heroes[hero_name]['MP'] >= mp_needed:
            heroes[hero_name]['MP'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(commands[2])
        attacker = commands[3]
        heroes[hero_name]['HP'] -= damage
        if heroes[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

    elif command == "Recharge":
        amount = int(commands[2])
        if amount + heroes[hero_name]['MP'] > 200:
            needed_amount = 200 - heroes[hero_name]['MP']
            print(f"{hero_name} recharged for {needed_amount} MP!")
            heroes[hero_name]['MP'] = 200
        else:
            heroes[hero_name]['MP'] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(commands[2])
        if amount + heroes[hero_name]['HP'] > 100:
            needed_amount = 100 - heroes[hero_name]['HP']
            print(f"{hero_name} healed for {needed_amount} HP!")
            heroes[hero_name]['HP'] = 100
        else:
            heroes[hero_name]['HP'] += amount
            print(f"{hero_name} healed for {amount} HP!")

for heroe, points in heroes.items():
    print(f"{heroe}")
    print(f" HP: {points['HP']}")
    print(f" MP: {points['MP']}")