# health = 100
# bitcoins = 0
# room = 0
#
# command = input().split("|")
# dead = False
#
# for current in command:
#     current_command = current.split()[0]
#     current_number = int(current.split()[1])
#     room += 1
#
#     if current_command == "potion":
#         if health + current_number > 100:
#             amount = 100 - health
#             health = 100
#         else:
#             health += current_number
#             amount = current_number
#         print(f"You healed for {amount} hp.")
#         print(f"Current health: {health} hp.")
#
#     elif current_command == "chest":
#         bitcoins += current_number
#         print(f"You found {current_number} bitcoins.")
#
#     else:
#         health -= current_number
#         if health > 0:
#             print(f"You slayed {current_command}.")
#         else:
#             dead = True
#             print(f"You died! Killed by {current_command}.")
#             print(f"Best room: {room}")
#
#     if dead:
#         break
#
# if not dead:
#     print("You've made it!")
#     print(f"Bitcoins: {bitcoins}")
#     print(f"Health: {health}")




health = 100
bitcoins = 0
room = 0

command = input().split("|")
dead = False

for current in command:
    current_command = current.split()[0]
    current_number = int(current.split()[1])
    room += 1

    if current_command == "potion":
        if health + current_number > 100:
            amount = 100 - health
            health = 100
        else:
            health += current_number
            amount = current_number
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif current_command == "chest":
        bitcoins += current_number
        print(f"You found {current_number} bitcoins.")

    else:
        health -= current_number
        if health > 0:
            print(f"You slayed {current_command}.")
        else:
            dead = True
            print(f"You died! Killed by {current_command}.")
            print(f"Best room: {room}")

    if dead:
        break

if not dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")