# First solution of the problem:

collected_items = input().split(", ")
command = input()

while command != "Craft!":
    current_command = command.split(" - ")
    action = current_command[0]
    item = current_command[1]
    if action == "Collect":
        if item not in collected_items:
            collected_items.append(item)
    elif action == "Drop":
        if item in collected_items:
            collected_items.remove(item)
    elif action == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in collected_items:
            idx = collected_items.index(old_item)  # collected_items.insert(collected_items.index(old_item) + 1, new_item)
            collected_items.insert(idx + 1, new_item)

    else:
        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)

    command = input()

new_collected_items = ", ".join(collected_items)
print(new_collected_items)







# Second solution of the problem:

collected_items = input().split(", ")

while True:
    data = input()

    if data == "Craft!":
        break

    current_command = data.split(" - ")
    action = current_command[0]
    item = current_command[1]

    if action == "Collect":
        if item not in collected_items:
            collected_items.append(item)

    elif action == "Drop":
        if item in collected_items:
            collected_items.remove(item)

    elif action == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in collected_items:
            idx = collected_items.index(old_item)  # collected_items.insert(collected_items.index(old_item) + 1, new_item)
            collected_items.insert(idx + 1, new_item)

    else:
        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)

print(", ".join(collected_items))
