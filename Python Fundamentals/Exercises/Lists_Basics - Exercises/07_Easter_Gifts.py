names_of_the_gifts = input().split()
command = input()

while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == "OutOfStock":
        for index in range(len(names_of_the_gifts)):
            if names_of_the_gifts[index] == current_gift:
                names_of_the_gifts[index] = "None"
    elif current_command[0] == "Required":
        index = int(current_command[2])
        if 0 <= index < len(names_of_the_gifts):
            names_of_the_gifts[index] = current_gift
    elif current_command[0] == "JustInCase":
        names_of_the_gifts[-1] = current_gift
    command = input()

for gifts in names_of_the_gifts:
    if gifts != "None":
        print(gifts, end=" ")
