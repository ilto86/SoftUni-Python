numbers = [int(num) for num in input().split()]

while True:
    data = input()
    if data == "END":
        break

    commands = data.split()
    command = commands[0]
    next_command = commands[1]

    if command == "add":
        nums_collection = [int(num) for num in commands if num.isdigit()]
        nums_collection.reverse()
        for nums in nums_collection:
            numbers.insert(0,nums)

    elif command == "remove" and next_command == "greater":
        value = int(commands[3])
        numbers = [num for num in numbers if num <= value]

    elif command == "replace":
        value = int(commands[1])
        replacement = int(commands[2])
        if value in numbers:
            idx = numbers.index(value)
            numbers[idx] = replacement

    elif command == "remove" and next_command == "at":
        index = int(commands[3])
        if 0 <= index < len(numbers):
            numbers.pop(index)

    elif command == "find" and next_command == "even":
        even_nums = [num for num in numbers if num % 2 == 0]
        even_nums = [str(num) for num in even_nums]
        print(" ".join(even_nums))

    elif command == "find" and next_command == "odd":
        odd_nums = [num for num in numbers if num % 2 != 0]
        odd_nums = [str(num) for num in odd_nums]
        print(" ".join(odd_nums))

numbers = [str(num) for num in numbers]
print(", ".join(numbers))