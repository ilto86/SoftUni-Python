# from collections import deque
#
#
# elf_energy = deque([int(x) for x in input().split()])
# box_of_materials = [int(x) for x in input().split()]
#
# toys = 0
# spent_energy = 0
# count = 0
#
# while elf_energy and box_of_materials:
#     while elf_energy and elf_energy[0] < 5:
#         elf_energy.popleft() # current elf's energy is less than 5 units, he does NOT TAKE a box and Remove it
#
#     if not elf_energy:
#         break
#
#     count += 1
#     energy = elf_energy.popleft()
#     box = box_of_materials.pop()
#
#     toys_created = 1    # elf must makes given amount of the toy
#     needed_energy = box # elf needs energy equal to the number of materials to makes the toy
#     cookie = 1  # After every turn elf eats a cookie which increases his energy by 1
#
#     if count % 3 == 0:
#         toys_created += 1   # elf manages to create 2 toys
#         needed_energy *= 2  # elf tries his best to be creative, and he will need twice as much energy as usual
#         cookie = 1
#     if count % 5 == 0:
#         toys_created = 0    # elf is clumsy, he breaks them
#         cookie = 0  #  elf doesn't get a cookie reward while is clumsy and have to break the toy when he just made it
#
#     if energy >= needed_energy:
#         energy -= needed_energy
#         spent_energy += needed_energy
#         toys += toys_created
#         energy += cookie
#         elf_energy.append(energy)   # goes to the end of the line, preparing for the upcoming boxes
#     else:
#         energy *= 2 # elf drinks a hot chocolate which doubles his energy
#         elf_energy.append(energy)   # goes to the end of the line, preparing for the upcoming boxes
#         box_of_materials.append(box)
#
# print(f"Toys: {toys}")
# print(f"Energy: {spent_energy}")
#
# if elf_energy:
#     print(f"Elves left: {', '.join([str(x) for x in elf_energy])}")
# if box_of_materials:
#     print(f"Boxes left: {', '.join([str(x) for x in box_of_materials])}")









from collections import deque


elfs_energy = deque([int(x) for x in input().split()])
materials_box = [int(x) for x in input().split()]

toys = 0
energy_spent = 0
day_count = 0

while elfs_energy and materials_box:
    elf = elfs_energy.popleft()
    box = materials_box.pop()

    cookie = 1
    hot_chocolate = 2
    needed_energy = box
    toys_make = 1

    if elf < 5:
        materials_box.append(box)
        continue

    else:
        day_count += 1

        if day_count % 3 == 0:
            needed_energy *= 2
            toys_make = 2

        if day_count % 5 == 0:
            toys_make = 0
            cookie = 0

        if elf >= needed_energy:
            elf -= needed_energy
            toys += toys_make
            energy_spent += needed_energy
            elf += cookie
            elfs_energy.append(elf)
        else:
            elf *= hot_chocolate
            elfs_energy.append(elf)
            materials_box.append(box)

print(f"Toys: {toys}")
print(f"Energy: {energy_spent}")

if elfs_energy:
    print(f"Elves left: {', '.join([str(x) for x in elfs_energy])}")
if materials_box:
    print(f"Boxes left: {', '.join([str(x) for x in materials_box])}")