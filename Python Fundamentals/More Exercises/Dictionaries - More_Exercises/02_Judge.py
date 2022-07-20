# def update_users(users, user, points):
# 	if user not in users:
# 		users[user] = points
# 	else:
# 		users[user] += points
# 	return users
#
#
# def update_contests(contests, users, user, contest, points):
# 	if contest not in contests:
# 		contests[contest] = {user: points}
# 	else:
# 		if user in contests[contest]:
# 			users[user] -= contests[contest][user]
# 			if contests[contest][user] > points:
# 				points = contests[contest][user]
# 		contests[contest][user] = points
# 	return contests, points
#
#
# def print_contests(contests):
# 	for contest, results in contests.items():
# 		print(f"{contest}: {len(results)} participants")
# 		position = 1
# 		results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
# 		for user, points in results.items():
# 			print(f"{position}. {user} <::> {points}")
# 			position += 1
#
#
# def print_users(users):
# 	users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
# 	position = 1
# 	print("Individual standings:")
# 	for user, points in users.items():
# 		print(f"{position}. {user} -> {points}")
# 		position += 1
#
#
# def main():
# 	contests = {}
# 	users = {}
#
# 	while True:
# 		data = input()
# 		if data == "no more time":
# 			break
# 		user, contest, points = data.split(" -> ")
# 		points = int(points)
# 		contests, points = update_contests(contests, users, user, contest, points)
# 		users = update_users(users, user, points)
#
# 	print_contests(contests)
# 	print_users(users)
#
#
# main()



# command = input()
# contests = {}
# individual_sum_grades = {}
#
# def validate_key_existance(dictionary, key, default_value = 0):
#     if key not in dictionary:
#         dictionary[key] = default_value
#
# # contests{contest:{student:points}}
# while command != "no more time":
#     student = command.split(" -> ")[0]
#     contest = command.split(" -> ")[1]
#     points = int(command.split(" -> ")[2])
#
#     if contest not in contests:
#         contests[contest] = {student: points}
#         validate_key_existance(individual_sum_grades, student)
#         individual_sum_grades[student] += points
#
#     else:
#         if student in contests[contest]:
#             if contests[contest][student] < points:
#                 contests[contest][student] = points
#                 validate_key_existance(individual_sum_grades, student)
#                 individual_sum_grades[student] = points
#
#         else:
#             contests[contest][student] = points
#             validate_key_existance(individual_sum_grades, student)
#             individual_sum_grades[student] += points
#     command = input()
#
# for key, inner_map in contests.items():
#     print(f'{key}: {len(inner_map)} participants')
#     count = 0
#     inner_map = dict(sorted(inner_map.items(), key=lambda x: (-x[1], x[0])))
#     for key, value in inner_map.items():
#         count += 1
#         print(f'{count}. {key} <::> {value}')
#
# individual_sum_grades = dict(sorted(individual_sum_grades.items(), key=lambda x: (-x[1], x[0])))
# print("Individual standings:")
# count = 0
# for key, value in individual_sum_grades.items():
#     count += 1
#     print(f'{count}. {key} -> {value}')


contests = {}
ranking = {}

command = input()

while command != "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {username: points}
    if contest in contests:
            if username in contests[contest]:
                if points > contests[contest][username]:
                    contests[contest][username] = points
            else:
                contests[contest][username] = points

    command = input()

for key, value in contests.items():
    print(f"{key}: {len(value)} participants")
    count = 0
    value = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
    for k, v in value.items():
        count += 1
        if k not in ranking:
            ranking[k] = v
        else:
            ranking[k] += v
        print(f'{count}. {k} <::> {v}')

ranking = dict(sorted(ranking.items(), key=lambda x: (-x[1], x[0])))
print("Individual standings:")
count = 0
for key, value in ranking.items():
    count += 1
    print(f'{count}. {key} -> {value}')