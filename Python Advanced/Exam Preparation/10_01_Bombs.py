from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = deque([int(x) for x in input().split(", ")])
filled_bomb_pouch = False

bombs = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_effects and bomb_casings:
    bomb_effect = bomb_effects[0]
    bomb_casing = bomb_casings[-1]

    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        filled_bomb_pouch = True
        break

    if sum([bomb_effect, bomb_casing]) == 40:
        bombs["Datura Bombs"] += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    elif sum([bomb_effect, bomb_casing]) == 60:
        bombs["Cherry Bombs"] += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    elif sum([bomb_effect, bomb_casing]) == 120:
        bombs["Smoke Decoy Bombs"] += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    else:
        bomb_casings[-1] -= 5

if filled_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for key, value in bombs.items():
    print(f"{key}: {value}")