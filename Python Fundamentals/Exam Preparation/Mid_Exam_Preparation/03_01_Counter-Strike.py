# First solution of the problem:

energy = int(input())

command = input()
won_battles = 0
enough_energy = True

while not command == "End of battle":

    if int(command) > energy:
        enough_energy = False
        break
    else:
        energy -= int(command)
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles

    command = input()

if enough_energy:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")



    
    
    
    
# Second solution of the problem:

initial_energy = int(input())
won_battle = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won_battle}. Energy left: {initial_energy}")
        break

    distance = int(command)

    if distance > initial_energy:
        print(f"Not enough energy! Game ends with {won_battle} won battles and {initial_energy} energy")
        break
    else:
        initial_energy -= distance
        won_battle += 1
        if won_battle % 3 == 0:
            initial_energy += won_battle
