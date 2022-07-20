# participants_list = input().split(", ")
# racers_dict = {}
#
# while True:
#     command = input()
#     if command == "end of race":
#         break
#
#     racer = [r for r in command if r.isalpha()]
#     racer = ''.join(racer)
#     digits = [int(d) for d in command if d.isdigit()]
#     digits = sum(digits)
#
#     if racer in participants_list:
#         if racer not in racers_dict:
#             racers_dict[racer] = digits
#         else:
#             racers_dict[racer] += digits
#
# sorted_racers_dict = dict(sorted(racers_dict.items(), key=lambda x: x[1], reverse=True))
#
# counter = 0
#
# for k, v in sorted_racers_dict.items():
#     counter += 1
#     if counter == 4:
#         break
#     if counter == 1:
#         print(f"1st place: {k}")
#     elif counter == 2:
#         print(f"2nd place: {k}")
#     elif counter == 3:
#         print(f"3rd place: {k}")




import re

names_list = input().split(', ')
names = {}
text = input()
pattern_1 = r"([a-zA-Z])"
pattern_2 = r"(\d)"
while not text == 'end of race':
    racer = ''.join(re.findall(pattern_1, text))
    points = sum([int(x) for x in re.findall(pattern_2, text)])
    if racer in names_list:
        if racer not in names.keys():
            names[racer] = 0
        names[racer] += points
    text = input()
names = sorted(names.items(), key=lambda x: -x[1])
print(f'1st place: {names[0][0]}')
print(f'2nd place: {names[1][0]}')
print(f'3rd place: {names[2][0]}')




# from re import findall
#
# participants = input().split(", ")
# results = {k: 0 for k in participants}
#
# data = input()
# while not data == "end of race":
#     name = "".join(findall(r"[A-Za-z]", data))
#     distance = sum([int(s) for s in findall(r"[\d]", data)])
#     if name in results:
#         results[name] += distance
#     data = input()
#
# top_runners_list = sorted(results.items(), key=lambda x: -x[1])
# print(f"1st place: {top_runners_list[0][0]}")
# print(f"2nd place: {top_runners_list[1][0]}")
# print(f"3rd place: {top_runners_list[2][0]}")






# import re
#
# l_pattern = r'[A-Za-z]'
# d_pattern = r'\d'
#
# participants = input().split(', ')
# race = {name: 0 for name in participants}
#
# while True:
#     data = input()
#     if data == 'end of race':
#         break
#     letters = re.findall(l_pattern, data)
#     digits = re.findall(d_pattern, data)
#     name = ''.join(letters)
#     distance = sum(map(int, digits))
#     if name in race:
#         race[name] += distance
#
# count = 1
# position = ''
# for participant, distance in sorted(race.items(), key=lambda x: -x[1]):
#     if count == 4:
#         break
#     position = '1st' if count == 1 else ('2nd' if count == 2 else '3rd')
#     print(f'{position} place: {participant}')
#     count += 1