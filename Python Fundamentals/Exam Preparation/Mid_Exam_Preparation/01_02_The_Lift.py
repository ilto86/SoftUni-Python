people = int(input())
lift = [int(x) for x in input().split(" ")]

for i in range(len(lift)):
    while not lift[i] == 4:
        if people > 0:
            lift[i] += 1
            people -= 1
        else:
            break

if people <= 0 and sum(lift) < len(lift) * 4:
    print("The lift has empty spots!")
elif people > 0 and sum(lift) == len(lift) * 4:
    print(f"There isn't enough space! {people} people in a queue!")

lift = [str(x) for x in lift]
print(f"{' '.join(lift)}")



people = int(input())
lift = [int(x) for x in input().split()]
max_people = 4

for i in range(len(lift)):
    for p in range(5):
        if int(lift[i]) < max_people and people > 0:
            lift[i] += 1
            people -= 1
        continue
    if sum(lift) == len(lift) * 4:
        break


if people == 0 and sum(lift) < len(lift) * 4:
    print("The lift has empty spots!")
elif people > 0 and sum(lift) == len(lift) * 4:
    print(f"There isn't enough space! {people} people in a queue!")

lift = [str(x) for x in lift]
print(f"{' '.join(lift)}")



people = int(input())
lift = [int(x) for x in input().split()]

for cab in range(len(lift)):
    if lift[cab] == 4:
        continue
    elif lift[cab] < 4 and people > 0:
        people -= 1
        lift[cab] += 1
        if lift[cab] < 4 and people > 0:
            people -= 1
            lift[cab] += 1
            if lift[cab] < 4 and people > 0:
                people -= 1
                lift[cab] += 1
                if lift[cab] < 4 and people > 0:
                    people -= 1
                    lift[cab] += 1


if people == 0 and sum(lift) < len(lift) * 4:
    print("The lift has empty spots!")

elif people > 0 and sum(lift) == len(lift) * 4:
    print(f"There isn't enough space! {people} people in a queue!")

lift = [str(x) for x in lift]
print(f"{' '.join(lift)}")