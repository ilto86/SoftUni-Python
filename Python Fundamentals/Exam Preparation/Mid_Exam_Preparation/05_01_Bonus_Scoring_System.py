from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

top_student = 0
top_attended = 0

for _ in range(number_of_students):
    count_of_attendances = int(input())
    total_bonus = count_of_attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus > top_student:
        top_student = total_bonus
    if count_of_attendances > top_attended:
        top_attended = count_of_attendances

print(f"Max Bonus: {ceil(top_student)}.")
print(f"The student has attended {ceil(top_attended)} lectures.")