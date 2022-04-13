# First solution of the problem:

targets = input().split()
targets = list(map(int, targets))

line = input()

while line != "End":
    command_list = line.split()
    command = command_list[0]
    index = int(command_list[1])
    value = int(command_list[2])

    if command == "Shoot" and index >= 0 and index < len(targets):
        current_target = targets[index]
        current_target -= value
        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target

    elif command == "Add":
        if index >= 0 and index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    line = input()

targets = list(map(str, targets))
output = "|".join(targets)
print(output)






# Second solution of the problem:

numbers = [int(num) for num in input().split()]

while True:
    data = input()
    if data == "End":
        break

    commands = data.split()
    command, index = commands[0], int(commands[1])

    if command == "Shoot" and 0 <= index < len(numbers):
        power = int(commands[2])
        numbers[index] -= power
        if numbers[index] <= 0:
            numbers.pop(index)

    elif command == "Strike":
        radius = int(commands[2])
        if 0 <= index - radius and index + radius < len(numbers):
            numbers = numbers[:index - radius] + numbers[index + radius + 1:]
        else:
            print("Strike missed!")

    elif command == "Add":
        value = int(commands[2])
        if 0 <= index < len(numbers):
            numbers.insert(index, value)
        else:
            print("Invalid placement!")

numbers = [str(num) for num in numbers]
print("|".join(numbers))
