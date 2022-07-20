string = input()

while True:
    decrypting = input()

    if decrypting == "Finish":
        break

    commands = decrypting.split()
    command = commands[0]

    if command == "Replace":
        current_char = commands[1]
        new_char = commands[2]
        if current_char in string:
            string = string.replace(current_char, new_char)
            print(string)

    elif command == "Cut":
        start_index = int(commands[1])
        end_index = int(commands[2])
        if 0 <= start_index <= end_index < len(string):
            string = string[:start_index] + string[end_index + 1:]
            print(string)
        else:
            print("Invalid indices!")

    elif command == "Make":
        upper_or_lower = commands[1]
        if upper_or_lower == "Upper":
            string = string.upper()
            print(string)
        else:
            string = string.lower()
            print(string)

    elif command == "Check":
        charecter = commands[1]
        if charecter in string:
            print(f"Message contains {charecter}")
        else:
            print(f"Message doesn't contain {charecter}")

    elif command == "Sum":
        start_index = int(commands[1])
        end_index = int(commands[2])
        char_sum = 0
        if 0 <= start_index <= end_index < len(string):
            for num in range(start_index, end_index + 1):
                char_sum += ord(string[num])
            print(char_sum)
        else:
            print("Invalid indices!")