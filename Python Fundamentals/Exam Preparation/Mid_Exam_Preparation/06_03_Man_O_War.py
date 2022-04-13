# First solution of the problem:

pirate_ship = [int(x) for x in input().split(">")]
warship = list(map(int, input().split(">")))
maximum_health = int(input())

condition = True

while True:
    commands = input().split()
    command = commands[0]

    if command == "Retire":
        break

    elif command == "Status":
        need_repair_soon = 0.2 * maximum_health
        count = 0
        for n in pirate_ship:
            if n < need_repair_soon:
                count += 1
        print(f"{count} sections need repair." )

    elif command == "Fire":
        index = int(commands[1])
        damage = int(commands[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                condition = False
                break

    elif command == "Defend":
        start_index = int(commands[1])
        end_index = int(commands[2])
        damage = int(commands[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for section in range(start_index, end_index + 1):
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    condition = False
                    break

    elif command == "Repair":
        index = int(commands[1])
        health = int(commands[2])
        if  0 <= index < len(pirate_ship):
            if (pirate_ship[index] + health) < maximum_health:
                pirate_ship[index] += health
            else:
                pirate_ship[index] = maximum_health


if condition:
    pirate_ship_sum = sum(pirate_ship)
    warship_sum = sum(warship)
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {warship_sum}")



    
    
    
# Second solution of the problem:

pirate_ships = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))


maximum_health = int(input())
condition = True

while True:
    commands = input().split(' ')
    command = commands[0]
    
    if command == 'Retire':
        break
    
    elif command == 'Fire':
        index = int(commands[1])
        damage = int(commands[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                condition = False
                print('You won! The enemy ship has sunken.')
                break
    
    elif command == 'Defend':
        start_index = int(commands[1])
        end_index = int(commands[2])
        damage = int(commands[3])
        if 0 <= start_index < len(pirate_ships) and 0 <= end_index < len(pirate_ships):
            for i, j in enumerate(pirate_ships[start_index:end_index + 1]):
                pirate_ships[i] -= damage
                if pirate_ships[i] <= 0:
                    condition = False
                    print('You lost! The pirate ship has sunken.')
                    break

    elif command == 'Repair':
        index = int(commands[1])
        health = int(commands[2])
        if 0 <= index < len(pirate_ships):
            if (pirate_ships[index] + health) < maximum_health:
                pirate_ships[index] += health
            else:
                pirate_ships[index] = maximum_health

    elif command == 'Status':
        counter = 0
        for i in pirate_ships:
            if i < maximum_health * 0.2:
                counter += 1
        print(f'{counter} sections need repair.')

if condition:
    print(f'Pirate ship status: {sum(pirate_ships)}')
    print(f'Warship status: {sum(warship)}')
