sequence_of_elements = [el for el in input().split()]
combination = input()
number_moves_until_now = 0

while combination != "end":
    number_moves_until_now += 1
    combination = combination.split()
    combi_1 = int(combination[0])
    combi_2 = int(combination[1])

    if combi_1 == combi_2 or combi_1 not in range(len(sequence_of_elements)) or combi_2 not in range(len(sequence_of_elements)):
        half_size = len(sequence_of_elements) // 2  # half_size = int(len(sequence_of_elements)) / 2
        left_side = sequence_of_elements[:half_size]
        right_side = sequence_of_elements[half_size:]
        left_side.append(f"-{number_moves_until_now}a")
        left_side.append(f"-{number_moves_until_now}a")
        sequence_of_elements = left_side + right_side
        print("Invalid input! Adding additional elements to the board")


    elif sequence_of_elements[combi_1] == sequence_of_elements[combi_2]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[combi_1]}!")
        sequence_of_elements = [el for el in sequence_of_elements if not el == sequence_of_elements[combi_1] or not el == sequence_of_elements[combi_2]]
    else:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {number_moves_until_now} turns!")
        break

    combination = input()

if len(sequence_of_elements) > 0:
    print("Sorry you lose :(")
    print(f"{' '.join(sequence_of_elements)}")






# elements = [i for i in input().split()]
#
# moves = 0
#
# while True:
#     command = input()
#     if command == "end":
#         break
#
#     [el_1, el_2] = command.split()
#     el_1 = int(el_1)
#     el_2 = int(el_2)
#     moves += 1
#     if el_1 == el_2 or el_1 not in range(len(elements)) or el_2 not in range(len(elements)):
#         elements.insert(int(len(elements) // 2), f"-{moves}a")
#         elements.insert(int(len(elements) // 2+1), f"-{moves}a")
#         print("Invalid input! Adding additional elements to the board")
#         continue
#     if elements[el_1] == elements[el_2]:
#         print(f"Congrats! You have found matching elements - {elements[el_1]}!")
#         elements = [el for el in elements if not el == elements[el_1] or not el == elements[el_2]]
#     else:
#         print("Try again!")
#     if not elements:
#         print(f"You have won in {moves} turns!")
#         break
#
# if len(elements) > 0:
#     print("Sorry you lose :(")
#     print(f"{' '.join(elements)}")


sequence_of_elements = [x for x in input().split()]
moves = 0
data = input()

while data != "end":
    indices = data.split()
    idx_1 = int(indices[0])
    idx_2 = int(indices[1])
    moves += 1

    if idx_1 == idx_2 or idx_1 not in range(len(sequence_of_elements)) or idx_2 not in range(len(sequence_of_elements)):
        half_size = len(sequence_of_elements) // 2
        left_side = sequence_of_elements[:half_size]
        right_side = sequence_of_elements[half_size:]
        left_side.append(f"-{moves}a")
        left_side.append(f"-{moves}a")
        sequence_of_elements = left_side + right_side
        print("Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[idx_1] == sequence_of_elements[idx_2]:
        element = sequence_of_elements[idx_1]
        print(f"Congrats! You have found matching elements - {element}!")
        sequence_of_elements.remove(element)
        sequence_of_elements.remove(element)
    else:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {moves} turns!")
        break

    data = input()

if sequence_of_elements:
    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))