# command = input()
# results = {}
# submissions = {}
#
# def validate_key_existance(dictionary, key, default_value = 0):
#     if key not in dictionary:
#         dictionary[key] = default_value
#
# def print_dict(dictionary, template):
#     for k, v in dictionary.items():
#         print(template.format(k, v))
#
# while command != "exam finished":
#     args = command.split("-")
#     name = args[0]
#
#     if args[1] == "banned":
#         del results[name]
#     else:
#         language = args[1]
#         points = int(args[2])
#         validate_key_existance(results, name)
#         if results[name] < points:
#             results[name] = points
#         validate_key_existance(submissions,language)
#         submissions[language] += 1
#
#     command = input()
#
# results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
# submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))
#
# print("Results:")
# print_dict(results, "{} | {}")
# print("Submissions:")
# print_dict(submissions, "{} - {}")




# def validate_key_existance(dictionary, key, default_value = 0):
#     if key not in dictionary:
#         dictionary[key] = default_value
#
# def print_dict(dictionary, template):
#     for k, v in dictionary.items():
#         print(template.format(k, v))
#
#
# command = input()
# results = {}
# submissions = {}
#
# while command != "exam finished":
#     args = command.split("-")
#     name = args[0]
#
#     if args[1] == "banned":
#         del results[name]
#     else:
#         language = args[1]
#         points = int(args[2])
#         validate_key_existance(results, name)
#         if results[name] < points:
#             results[name] = points
#         validate_key_existance(submissions,language)
#         submissions[language] += 1
#
#     command = input()
#
# print("Results:")
# print_dict(results, "{} | {}")
# print("Submissions:")
# print_dict(submissions, "{} - {}")




# command = input().split("-")
#
# user_dict = {}
# points_dict = {}
#
# while command[0] != "exam finished":
#     username = command[0]
#     language = command[1]
#     if language == "banned":
#         user_dict.pop(username)
#         command = input().split("-")
#         continue
#     points = int(command[2])
#
#     if username not in user_dict:
#         user_dict[username] = [points]
#     else:
#         user_dict[username] += [points]
#     if language not in points_dict:
#         points_dict[language] = [points]
#     else:
#         points_dict[language] += [points]
#
#     command = input().split("-")
#
# sorted_user_dict = dict(sorted(user_dict.items(), key= lambda x: (- max(x[1]), x[0])))
# sorted_points_dict = dict(sorted(points_dict.items(), key= lambda x: (- len(x), x[0])))
#
# print(f"Results:")
#
# for k, v in sorted_user_dict.items():
#     max_val = max(v)
#     print(f"{k} | {max_val}")
#
# print(f"Submissions:")
#
# for a, b in sorted_points_dict.items():
#     print(f"{a}", end=' - ')
#     print(f"{len(b)}")




command = input().split("-")

user_dict = {}
points_dict = {}

while command[0] != "exam finished":
    username = command[0]
    language = command[1]
    if language == "banned":
        user_dict.pop(username)
        command = input().split("-")
        continue
    points = int(command[2])

    if username not in user_dict:
        user_dict[username] = [points]
    else:
        user_dict[username] += [points]
    if language not in points_dict:
        points_dict[language] = [points]
    else:
        points_dict[language] += [points]

    command = input().split("-")

# sorted_user_dict = dict(sorted(user_dict.items(), key= lambda x: (- max(x[1]), x[0])))
# sorted_points_dict = dict(sorted(points_dict.items(), key= lambda x: (- len(x), x[0])))

print(f"Results:")

for k, v in user_dict.items():             #  for k, v in sorted_user_dict.items():
    max_val = max(v)
    print(f"{k} | {max_val}")

print(f"Submissions:")

for a, b in points_dict.items():    #  for a, b in sorted_points_dict.items():
    print(f"{a}", end=' - ')
    print(f"{len(b)}")