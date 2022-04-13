first = int(input())
second = int(input())
third = int(input())
students_count = int(input())

all_employees_efficiency = first + second + third

time = 0
while True:
    if students_count <= 0:
        break
    time += 1
    if time % 4 == 0:
        continue
    else:
        students_count -= all_employees_efficiency
print(f"Time needed: {time}h.")
