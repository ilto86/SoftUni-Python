coffee_list = input().split()
count = int(input())

for _ in range(count):

    current_command = input().split()
    item = current_command[0]

    if item == "Include":
        item1 = current_command[1]
        coffee_list.append(item1)

    elif item == "Remove":
        item1 = current_command[1]
        item2 = int(current_command[2])
        if item1 == "first" and item2 < len(coffee_list):
            index1 = 0
            index2 = item2
            for i in range(index2):
                coffee_list.pop(index1)
        elif item1 == "last" and item2 < len(coffee_list):
            index1 = -1
            index2 = item2
            for i in range(index2):
                coffee_list.pop(index1)

    elif item == "Prefer":
        item1 = int(current_command[1])
        item2 = int(current_command[2])
        if coffee_list[item1] in coffee_list and coffee_list[item2] in coffee_list:
            coffee_list[item1], coffee_list[item2] = coffee_list[item2], coffee_list[item1]

    else:
        if item == "Reverse":
            coffee_list.reverse()

print(f"Coffees:\n{' '.join(coffee_list)}")