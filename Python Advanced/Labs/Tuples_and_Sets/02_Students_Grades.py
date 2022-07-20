def avg(value):
    return sum(value) / len(value)


n = int(input())
student_strings = [input() for _ in range(n)]
students_grades = {}

for student_string in student_strings:
    student, grade_string = student_string.split()
    grade = float(grade_string)
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(grade)

for student, grades in students_grades.items():
    grades_formatted = " ".join(f'{grade:.2f}' for grade in grades)
    grades_avg = avg(grades)
    grades_avg_formatted = f"{grades_avg:.2f}"
    print(f"{student} -> {grades_formatted} (avg: {grades_avg_formatted})")








# n = int(input())
# grades = {}
#
# for _ in range(n):
#     name, grade_as_str = input().split()
#     grade = float(grade_as_str)
#     if name not in grades:
#         grades[name] = []
#     grades[name].append(grade)
#
# for data in grades.items():
#     print(f"{data[0]} -> {' '.join([f'{el:.2f}' for el in data[1]])} (avg: {sum(data[1]) / len(data[1]):.2f})")







# count = int(input())
#
# students = {}
#
# for _ in range(count):
#     student, grade = tuple(input().split())
#     if student not in students:
#         students[student] = []
#     students[student].append(float(grade))
#
# for key, value in students.items():
#     avarage = sum(value) / len(students[key])
#     value = ' '.join(map(lambda f: format(f, '.2f'), value))    # format function that makes str formatted to float number, but it is still string
#     print(f"{key} -> {value} (avg: {avarage:.2f})")








# count = int(input())
#
# students = {}
#
# for _ in range(count):
#     student, grade = input().split()
#     if student not in students:
#         students[student] = []
#     students[student].append(float(grade))
#
# for key, value in students.items():
#     avarage = sum(value) / len(value)
#     value = [f"{x:.2f}" for x in value]     # format function that makes float number formatted
#     print(f"{key} -> {' '.join(value)} (avg: {avarage:.2f})")

    # value = ' '.join(map(lambda f: format(f, '.2f'), value))    # format function that makes str formatted to float number, but it is still string
    # print(f"{key} -> {value} (avg: {avarage:.2f})")
