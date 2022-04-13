# First solution of the problem:

neighborhood = list(map(int, input().split("@")))
commands = input()

current_index_position = 0
cupids_last_position = 0
while True:
    command = commands.split()

    if command[0] == "Love!":
        break

    index = int(command[1]) + current_index_position
    if index >= len(neighborhood):
        index = 0

    if -1 < index < len(neighborhood):
        if neighborhood[index] > 0:
            neighborhood[index] -= 2
            if neighborhood[index] == 0:
                print(f"Place {index} has Valentine's day.")
        else:
            print(f"Place {index} already had Valentine's day.")
    cupids_last_position = index
    current_index_position = index

    commands = input()


result = [x for x in neighborhood if x == 0]
print(f"Cupid's last position was {cupids_last_position}.")

if len(result) != len(neighborhood):
    diff = abs(len(neighborhood) - len(result))
    print(f"Cupid has failed {diff} places.")
else:
    print("Mission was successful.")






    

    
# Second solution of the problem:

number_list = [int(num) for num in input().split("@")]
current_position = 0
last_position = 0

while True:
    data = input()

    if data == "Love!":
        break

    commands = data.split()
    index = int(commands[1]) + current_position

    if index >= len(number_list):
        index = 0

    if 0 <= index < len(number_list):
        if number_list[index] > 0:
            number_list[index] -= 2
            if number_list[index] == 0:
                print(f"Place {index} has Valentine's day.")
        else:
            print(f"Place {index} already had Valentine's day.")

    last_position = index
    current_position = index

result = [x for x in number_list if x == 0]
print(f"Cupid's last position was {last_position}.")

if len(result) != len(number_list):
    diff = abs(len(number_list) - len(result))
    print(f"Cupid has failed {diff} places.")
else:
    print("Mission was successful.")
