sequence_of_elements = [x for x in input().split()]
moves = 0
data = input()

while data != "end":
    indices = data.split()
    index_1 = int(indices[0])
    index_2 = int(indices[1])
    moves += 1

    if index_1 == index_2 or index_1 not in range(len(sequence_of_elements)) or index_2 not in range(len(sequence_of_elements)):
        half_size = len(sequence_of_elements) // 2
        left_side = sequence_of_elements[:half_size]
        right_side = sequence_of_elements[half_size:]
        left_side.append(f"-{moves}a")
        left_side.append(f"-{moves}a")
        sequence_of_elements = left_side + right_side
        print("Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[index_1] == sequence_of_elements[index_2]:
        element = sequence_of_elements[index_1]
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
