# first_employee_efficiency = int(input())
# second_employee_efficiency = int(input())
# third_employee_efficiency = int(input())
# students_count = int(input())
# time_count = 0
#
# per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
#
# while students_count > 0:
#     time_count += 1
#
#     if time_count % 4 == 0:
#         continue
#
#     students_count -= per_hour
#
# print(f"Time needed: {time_count}h.")




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


