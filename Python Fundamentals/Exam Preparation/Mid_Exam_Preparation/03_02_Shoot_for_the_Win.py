# First solution of the problem:

numbers = [int(num) for num in input().split()]
command = input()
shoot_a_targets = 0
substract = 0
collect = 0
target_num = 0
index = 0

while command != "End":
    targets = int(command)
    
    if targets > len(numbers) - 1:
        command = input()
        continue
    
    target_num = numbers[targets]
    index = 0
    
    for num in numbers:
        
        if num > numbers[targets] and numbers[targets] != -1:
            substract = num - numbers[targets]
            numbers[index] = substract
        
        elif 0 < num <= numbers[targets] and numbers[targets] != -1:
            
            if targets == index:
                index += 1
                continue
            
            collect = num + numbers[targets]
            numbers[index] = collect

        index += 1
        continue

    if numbers[targets] == target_num:
        target_num = -1
        shoot_a_targets += 1
        numbers[targets] = target_num

    command = input()

numbers = [str(num) for num in numbers]
output = " ".join(numbers)
print(f"Shot targets: {shoot_a_targets} -> {output}" )






# Second solution of the problem:

numbers = [int(num) for num in input().split()]
count = 0
while True:
    command = input()
    
    if command == "End":
        break

    index = int(command)
    
    if 0 <= index < len(numbers):
        targets_num = numbers[index]
        count += 1
        
        for idx, num in enumerate(numbers):

            if targets_num > 0 and idx != index and num != -1:

                if num > targets_num:
                    numbers[idx] -= targets_num

                elif num <= targets_num:
                    numbers[idx] += targets_num

            elif idx == index:
                continue

        numbers.pop(index)
        numbers.insert(index, -1)

numbers = [str(num) for num in numbers]
print(f"Shot targets: {count} -> {' '.join(numbers)}")
