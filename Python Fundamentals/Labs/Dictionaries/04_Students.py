# data = input()
#
# courses = {}
#
# while ":" in data:
#     student_name, id, course_name = data.split(":")
#     if course_name not in courses:
#         courses[course_name] = {}
#     courses[course_name][id] = student_name
#     data = input()
#
# searched_course = data
# searched_course_name_as_list = searched_course.split("_")
# searched_course = " ".join(searched_course_name_as_list)
#
# for course_name in courses:                            # for id, name in courses[searched_course].items():
#     if course_name == searched_course:                 #  for id, name in courses[searched_course].items():
#         for id, name in courses[course_name].items():  #  for id, name in courses[searched_course].items():
#             print(f"{name} - {id}")



text = input()

courses = dict()
while ":" in text:
    data = text.split(":")  # (name, id, course) = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][id] = name

    text = input()

text = text.replace("_", " ")

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")