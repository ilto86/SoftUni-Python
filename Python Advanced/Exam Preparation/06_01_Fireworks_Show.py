from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

enough_fireworks = False
while firework_effects and explosive_power:
    effect = firework_effects[0]
    power = explosive_power[-1]

    if effect <= 0:
        firework_effects.popleft()
        continue
    if power <= 0:
        explosive_power.pop()
        continue

    if (effect + power) % 3 == 0 and (effect + power) % 5 != 0 :
        firework_effects.popleft()
        explosive_power.pop()
        fireworks["Palm Fireworks"] += 1

        if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks[
            "Crossette Fireworks"] >= 3:
            enough_fireworks = True
            break

    elif (effect + power) % 5 == 0 and (effect + power) % 3 != 0 :
        firework_effects.popleft()
        explosive_power.pop()
        fireworks["Willow Fireworks"] += 1
        if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks[
            "Crossette Fireworks"] >= 3:
            enough_fireworks = True
            break

    elif (effect + power) % 3 == 0 and (effect + power) % 5 == 0 :
        firework_effects.popleft()
        explosive_power.pop()
        fireworks["Crossette Fireworks"] += 1
        if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks[
            "Crossette Fireworks"] >= 3:
            enough_fireworks = True
            break

    else:
        firework_effects.append(effect - 1)
        firework_effects.popleft()

if enough_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for k, v in fireworks.items():
    print(f"{k}: {v}")