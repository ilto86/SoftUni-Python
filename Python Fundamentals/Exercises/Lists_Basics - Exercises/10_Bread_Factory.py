# initial_energy = 100
# initial_coins = 100
#
# events = input().split("|")
#
# is_bankrupted = False
#
# for event in events:
#     event_info = event.split("-")
#
#     event_type = event_info[0]
#     event_number = int(event_info[1])
#
#     if event_type == "rest":
#         energy_gained = event_number
#
#         if initial_energy + event_number > 100:
#             energy_gained = 100 - initial_energy
#
#         initial_energy += energy_gained
#
#         print(f"You gained {energy_gained} energy.")
#         print(f"Current energy: {initial_energy}.")
#
#     elif event_type == "order":
#         if initial_energy - 30 >= 0:
#             initial_coins += event_number
#             initial_energy -= 30
#
#             print(f"You earned {event_number} coins.")
#         else:
#             initial_energy += 50
#
#             print("You had to rest!")
#     else:
#         if initial_coins - event_number > 0:
#             initial_coins -= event_number
#
#             print(f"You bought {event_type}.")
#         else:
#             print(f"Closed! Cannot afford {event_type}.")
#             is_bankrupted = True
#             break
#
# if not is_bankrupted:
#     print("Day completed!")
#     print(f"Coins: {initial_coins}")
#     print(f"Energy: {initial_energy}")



events = input().split("|")
energy = 100
coins = 100
close_condition = False

for event in events:
    current_event_elements = event.split("-")
    command = current_event_elements[0]
    number = int(current_event_elements[1])

    if command == "rest":
        if energy  >= 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif command == "order":
        if energy >= 30:
            print(f"You earned {number} coins.")
            energy -= 30
            coins += number
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            print(f"You bought {command}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {command}.")
            close_condition = True
            break

if not close_condition:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")