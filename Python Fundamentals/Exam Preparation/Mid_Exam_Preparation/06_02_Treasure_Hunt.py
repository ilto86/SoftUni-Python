treasure_chest = input().split("|")
commands = input()
failed_hunt = False

while commands != "Yohoho!":

    command = commands.split()

    if command[0] == "Loot":
        for item in command[1::]:  # [treasure_chest.insert(0, x) for x in command[1::] if x not in treasure_chest]
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif command[0] == "Drop":
        idx = int(command[1])
        if idx <= len(treasure_chest):
            item = treasure_chest.pop(idx)
            treasure_chest.append(item)

    elif command[0] == "Steal":
        theft = int(command[1])
        if theft >= len(treasure_chest):
            failed_hunt = True
            print(", ".join(treasure_chest))
        else:
            steal_treasure = []
            for s in range(theft):
                theft_treasure = treasure_chest.pop(-1)
                steal_treasure.append(theft_treasure)
            steal_treasure.reverse()
            print(f"{', '.join(steal_treasure)}")

    commands = input()

if not failed_hunt:
    lenght_treasure_chest = int(len(treasure_chest))
    current_treasure_chest = "".join(treasure_chest)
    average_treasure_gain = int(len(current_treasure_chest))
    total_gain = average_treasure_gain / lenght_treasure_chest
    print(f"Average treasure gain: {total_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")