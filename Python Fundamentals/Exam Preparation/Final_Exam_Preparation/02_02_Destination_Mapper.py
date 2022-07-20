# import re
#
# destination = input()
# travel_points = 0
#
# pattern = r"=([A-Z][a-zA-Z]{2,})=|/([A-Z][a-zA-Z]{2,})/"
#
# matches = re.findall(pattern,destination)
# matches = [tuple(x for x in i if x)[-1] for i in matches]
#
# for match in matches:
#     travel_points += len(match)
#
# new_match = ", ".join(matches)
# print(f"Destinations: {new_match}")
# print(f"Travel Points: {travel_points}")




# import re
#
# destination = input()
#
# new_destination = []
# travel_points = 0
#
# pattern = r"=([A-Z][a-zA-Z]{2,})=|/([A-Z][a-zA-Z]{2,})/"
#
# matches = re.findall(pattern,destination)
#
# for from_tuple in matches:
#     for each_word in from_tuple:
#         if each_word.isalpha():
#             new_destination.append(each_word)
#
# for place in new_destination:
#     travel_points += len(place)
#
# print(f"Destinations: {', '.join(new_destination)}")
# print(f"Travel Points: {travel_points}")




# import re
#
# text = input()
# destinations = []
# travel_points = 0
#
# pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
#
# matches = re.finditer(pattern, text)
#
#
# for match in matches:
#     destinations.append(match.group(2))
#
# for point in destinations:
#     travel_points += len(point)
#
# print(f"Destinations: {', '.join(destinations)}")
# print(f"Travel Points: {travel_points}")




# import re
#
#
# initial_text = input()
# destinations = []
# travel_points = 0
#
# pattern = r'((?<=[=])[A-Z][A-Za-z]{2,}(?=[=]))|((?<=[\\/])[A-Z][A-Za-z]{2,}(?=[\\/]))'
# matches = re.finditer(pattern, initial_text)
#
# for match in matches:
#     destinations.append(match.group())
#
# for points in destinations:
#     travel_points += len(points)
#
# print(f"Destinations: {', '.join(destinations)}")
# print(f"Travel Points: {travel_points}")





# import re
#
# text = input()
# regex = r"([=/])([A-Z][A-Za-z]{2,})\1"
#
# matches = re.finditer(regex, text)
# locations = list()
# points = 0
#
# for match in matches:
#     city = match[2]
#     locations.append(city)
#     points += len(city)
#
# output_locations = ", ".join(locations)
# print(f"Destinations: {output_locations}")
# print(f"Travel Points: {points}")




import re

text = input()

pattern = "=([A-Z][A-Za-z]{2,})=|/([A-Z][A-Za-z]{2,})/"
matches = re.findall(pattern,text)

places = ""
travel_points = 0
destinations = []

for match in matches:
    current_destination = [el for el in match if el != '']
    places = "".join(current_destination)
    travel_points += len(places)
    destinations.append(places)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")