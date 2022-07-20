# def get_contests():
# 	contests = {}
# 	while True:
# 		data = input()
# 		if data == "end of contests":
# 			break
# 		contest, password = data.split(":")
# 		contests[contest] = password
# 	return contests
#
#
# def get_users_data(contests):
# 	users = {}
# 	while True:
# 		data = input()
# 		if data == "end of submissions":
# 			break
# 		contest, password, username, points = data.split("=>")
# 		points = int(points)
# 		if contest not in contests or not password == contests[contest]:
# 			continue
# 		if username in users:
# 			if contest in users[username] and points < users[username][contest]:
# 				points = users[username][contest]
# 			users[username][contest] = points
# 		else:
# 			users[username] = {contest: points}
# 	return users
#
#
# def calc_total_points(users):
# 	users_total_points = {}
# 	for key, value in users.items():
# 		total_points = sum([score for score in value.values()])
# 		users_total_points[key] = total_points
# 	return users_total_points
#
#
# def print_best_candidate(users_total_points):
# 	best_candidate = max(users_total_points, key=lambda x: users_total_points[x])
# 	best_score = users_total_points[best_candidate]
# 	print(f"Best candidate is {best_candidate} with total {best_score} points.")
#
#
# def print_all_students(users):
# 	print("Ranking:")
# 	users = dict(sorted(users.items(), key=lambda x: x[0]))
# 	for username, values in users.items():
# 		print(username)
# 		values = dict(sorted(values.items(), key=lambda x: -x[1]))
# 		for contest, points in values.items():
# 			print(f"#  {contest} -> {points}")
#
#
# def main():
# 	contests = get_contests()
# 	users = get_users_data(contests)
# 	users_total_points = calc_total_points(users)
# 	print_best_candidate(users_total_points)
# 	print_all_students(users)
#
#
# main()






# command_contests = input()
# contests = {}
# ranking = {}
# while command_contests != "end of contests":
#     contest = command_contests.split(":")[0]
#     password = command_contests.split(":")[1]
#
#     if contest not in contests:
#         contests[contest] = password
#     command_contests = input()
#
# command_submissions = input()
#
# while command_submissions != "end of submissions":
#     contest = command_submissions.split("=>")[0]
#     password = command_submissions.split("=>")[1]
#     name = command_submissions.split("=>")[2]
#     points = int(command_submissions.split("=>")[3])
#
#     if contest in contests and contests[contest] == password:
#         if name not in ranking:
#             ranking[name] = {contest: points}
#         else:
#             if contest in ranking[name]:
#                 if points > ranking[name][contest]:
#                     ranking[name][contest] = points
#             else:
#                 ranking[name][contest] = points
#     command_submissions = input()
#
# ranking_sum = {k: sum(v_dict.values()) for k, v_dict in ranking.items()} # SUM THE VALUES OF NESTED DICTIONARY
# max_points_pair = max(ranking_sum.items(), key=lambda k: k[1]) # GET KEY-VALUE PAIR WITH LARGEST VALUE
#
# print(f'Best candidate is {max_points_pair[0]} with total {max_points_pair[1]} points.')
# print("Ranking:")
# ranking = dict(sorted(ranking.items()))
#
# for key, inner_map in ranking.items():
#     inner_map = dict(sorted(inner_map.items(), key=lambda x: (-x[1])))
#     print(key)
#     for k, v in inner_map.items():
#         print(f'#  {k} -> {v}')


# contests = {}  # contests {contest: password}
# submissions = {}  # submissions {user: {contest: points}}
#
# while True:
#     input_line = input()
#     if input_line == 'end of contests':
#         break
#     contest, password = input_line.split(':')
#     contests[contest] = password
#
# while True:
#     input_line = input()
#     if input_line == 'end of submissions':
#         break
#     contest, password, user, pts = input_line.split('=>')
#     if contest in contests and contests.get(contest) == password:
#         if user in submissions:
#             submissions[user][contest] = max(submissions[user].get(contest, 0), int(pts))
#         else:
#             submissions[user] = {contest: int(pts)}
#
# user_total_pts = sorted([(sum(submissions[user].values()), user) for user in submissions.keys()], reverse=True)
# print(f"Best candidate is {user_total_pts[0][1]} with total {user_total_pts[0][0]} points.")
#
# print('Ranking:')
# for user in sorted([user for user in submissions.keys()]):
#     user_submissions = [u_s for u_s in sorted(submissions[user].items(), key=lambda item: -item[1])]
#     output = [f'#  {contest} -> {points}' for (contest, points) in user_submissions]
#     print(user)
#     print(*output, sep='\n')




contest_data = input()
contests_dict = dict()

while contest_data != "end of contests":
    (contest, password) = contest_data.split(":")
    contests_dict[contest] = password
    contest_data = input()


submission_data = input()
users_dict = dict()

while submission_data != "end of submissions":
    (contest, password, user, points) = submission_data.split("=>")

    if contest in contests_dict and contests_dict[contest] == password:

            if user not in users_dict:
                users_dict[user] = dict()

            if contest not in users_dict[user]:
                users_dict[user][contest] = int(points)
            else:
                if users_dict[user][contest] < int(points):
                    users_dict[user][contest] = int(points)

    submission_data = input()

best_user = ""
best_points = 0

for user in users_dict.keys():
    total_points = sum(users_dict[user].values())
    if total_points > best_points:
        best_points = total_points
        best_user = user

print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")

for user in sorted(users_dict.keys()):
    print(user)
    for (contest, points) in sorted(users_dict[user].items(), key= lambda cp: -cp[1]):
        print(f"# {contest} -> {points}")