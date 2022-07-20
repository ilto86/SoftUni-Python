numbers = [int(num) for num in input().split()]

while True:
    data = input()
    if data == "END":
        break

    commands = data.split()
    command = commands[0]

    if command == "Change":
        painting_number = int(commands[1])
        new_painting_number = int(commands[2])
        if painting_number in numbers:
            idx = numbers.index(painting_number)
            numbers[idx] = new_painting_number

    elif command == "Hide":
        painting_number = int(commands[1])
        if painting_number in numbers:
            numbers.remove(painting_number)

    elif command == "Switch":
        painting_number_1 = int(commands[1])
        painting_number_2 = int(commands[2])
        if painting_number_1 in numbers and painting_number_2 in numbers:
            idx_1 = numbers.index(painting_number_1)
            idx_2 = numbers.index(painting_number_2)
            numbers[idx_1], numbers[idx_2] = numbers[idx_2], numbers[idx_1]

    elif command == "Insert":
        index = int(commands[1])
        painting_number = int(commands[2])
        if 0 <= index + 1 < len(numbers):
            numbers.insert(index + 1, painting_number)

    elif command == "Reverse":
        numbers.reverse()

numbers = [str(num) for num in numbers]
print(" ".join(numbers))