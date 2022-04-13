# n = int(input())
#
# max_snowball_value = 0
# max_snowball_weight = 0
# max_snowball_time = 0
# max_snowball_quality = 0
#
# for i in range(n):
#     snowball_weight = int(input())
#     snowball_time = int(input())
#     snowball_quality = int(input())
#
#     snowball_value = (snowball_weight / snowball_time) ** snowball_quality
#
#     if snowball_value >= max_snowball_value:
#         max_snowball_value = snowball_value
#         max_snowball_weight = snowball_weight
#         max_snowball_time = snowball_time
#         max_snowball_quality = snowball_quality
#
# print(f"{max_snowball_weight} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})")




number_of_snowballs = int(input())
best_snowball_quality = 0
best_snowball_data = ''

for _ in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight / time) ** quality

    if result > best_snowball_quality:
     best_snowball_quality = result
     best_snowball_data = f'{weight} : {time} = {int(result)} ({quality})'

print(best_snowball_data)