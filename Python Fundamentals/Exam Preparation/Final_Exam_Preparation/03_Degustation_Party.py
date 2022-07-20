guests = {}
unliked_meals = 0
while True:
    data = input()
    if data == "Stop":
        break
    command = data.split("-")

    if command[0] == "Like":
        name = command[1]
        meal = command[2]
        if name not in guests:
            guests[name] = [meal]
        elif name in guests and meal not in guests[name]:
            guests[name].append(meal)
        elif meal in guests[name]:
            continue

    elif command[0] == "Dislike":
        name = command[1]
        meal = command[2]

        if name not in guests:
            print(f"{name} is not at the party.")

        else:
            if meal in guests[name]:
                unliked_meals += 1
                guests[name].remove(meal)
                print(f"{name} doesn't like the {meal}.")
            else:
                print(f"{name} doesn't have the {meal} in his/her collection.")

for person, meals in guests.items():
    print(f"{person}: {', '.join(meals)}")

print(f"Unliked meals: {unliked_meals}")