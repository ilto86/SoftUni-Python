sequence_of_targets = [int(num) for num in input().split()]

command = input()

while command != "End":
    current_command = command.split()[0]
    indices = int(command.split()[1])
    targets_manipulating = int(command.split()[2])

    if current_command == "Shoot":
        if indices in range(len(sequence_of_targets)):
            sequence_of_targets[indices] -= targets_manipulating
            if sequence_of_targets[indices] <= 0:
                sequence_of_targets.remove(sequence_of_targets[indices])

    elif current_command == "Add":
        if indices in range(len(sequence_of_targets)):
            sequence_of_targets.insert(indices, targets_manipulating)
        else:
            print("Invalid placement!")

    elif current_command == "Strike":
        if indices + targets_manipulating in range(len(sequence_of_targets)) and indices - targets_manipulating in range(len(sequence_of_targets)):
            sequence_of_targets = sequence_of_targets[:indices - targets_manipulating] + sequence_of_targets[indices + targets_manipulating + 1:]
        else:
            print("Strike missed!")

    command = input()

sequence_of_targets = [str(num) for num in sequence_of_targets]
print("|".join(sequence_of_targets))