# First solution of the problem:

array_values = [int(el) for el in input().split()]

command = input()

while command != "end":
    if command == "decrease":
        array_values = list(map(lambda x: x - 1, array_values))
    else:
        task = command.split()
        first_index = int(task[1])
        second_index = int(task[2])
        if task[0] == "swap":
            array_values[first_index], array_values[second_index] = array_values[second_index], array_values[first_index]
        elif task[0] == "multiply":
            array_values[first_index] = array_values[first_index] * array_values[second_index]

    command = input()

array_values = [str(el) for el in array_values]
print(", ".join(array_values))






# Second solution of the problem:

array_values = [int(num) for num in input().split()]

while True:
    data = input()
    if data == "end":
        break

    commands = data.split()
    command = commands[0]

    if command == "swap":
        index_1 = int(commands[1])
        index_2 = int(commands[2])
        array_values[index_1], array_values[index_2] = array_values[index_2], array_values[index_1]

    elif command == "multiply":
        index_1 = int(commands[1])
        index_2 = int(commands[2])
        array_values[index_1] = array_values[index_1] * array_values[index_2]

    elif command == "decrease":
        array_values = [num - 1 for num in array_values]

array_values = [str(num) for num in array_values]
print(", ".join(array_values))
