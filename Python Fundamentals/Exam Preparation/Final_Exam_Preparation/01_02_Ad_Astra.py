# import re
#
# initial_text = input()
#
# pattern = r'(?P<separator>#|\|)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<exp_date>\d{2}\/\d{2}\/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)'
#
# calories_per_day = 2000
#
# match = re.finditer(pattern, initial_text)
# food_info_list = []
# total_calories = 0
#
# for m in match:
#     result = m.groupdict()
#     food_info_list.append(result)
#
#     total_calories += int(m.group('calories'))
#
# days_to_last_in_space = total_calories // calories_per_day
#
# print(f"You have food to last you for: {days_to_last_in_space} days!")
#
# for item in food_info_list:
#     print(f"Item: {item['item']}, Best before: {item['exp_date']}, Nutrition: {item['calories']}")




# import re
#
# initial_text = input()
#
# pattern = r'(?P<separator>#|\|)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<exp_date>\d{2}\/\d{2}\/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)'
# calories_per_day = 2000
#
# match = re.finditer(pattern, initial_text)
# total_calories = 0
#
# for m in match:
#     total_calories += int(m.group('calories'))
#
# days_to_last_in_space = total_calories // calories_per_day
#
# print(f"You have food to last you for: {days_to_last_in_space} days!")
#
# match = re.finditer(pattern, initial_text)
#
# for mat in match:
#     print(f"Item: {mat.group('item')}, Best before: {mat.group('exp_date')}, Nutrition: {mat.group('calories')}")




# import re
#
# initial_text = input()
#
# pattern = r'(?P<separator>#|\|)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<exp_date>\d{2}\/\d{2}\/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)'
#
# calories_per_day = 2000
#
# match = re.finditer(pattern, initial_text)
# food_info_list = []
# total_calories = 0
#
# for m in match:
#     food_info_list.append([m.group('item'), m.group('exp_date'), int(m.group('calories'))])
#
#     total_calories += int(m.group('calories'))
#
# days_to_last_in_space = total_calories // calories_per_day
#
# print(f"You have food to last you for: {days_to_last_in_space} days!")
#
# for i in food_info_list:
#     print(f"Item: {i[0]}, Best before: {i[1]}, Nutrition: {i[2]}")



# import re
#
# data = input()
#
# pattern = r"([#\|])(?P<item>[a-zA-Z\s]+)\1(?P<exp_date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"
#
# valid_data = re.finditer(pattern, data)
# food_data = []
# total_calories = 0
# calories_per_day = 2000
#
# for match in valid_data:
#     food_data.append(match.groupdict())
#     calories = int(match["calories"])
#     total_calories += calories
#
# print(f"You have food to last you for: {total_calories // calories_per_day} days!")
# for el in food_data:
#     print(f"Item: {el['item']}, Best before: {el['exp_date']}, Nutrition: {el['calories']}")




# import re
#
# info = input()
#
# pattern = '\#([a-z A-Z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|' \
#           '\|([a-z A-Z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'
# result = re.findall(pattern, info)
# items = []
# calories = 0
#
# for item in result:
#     current_item = [el for el in item if el != '']
#     items.append(current_item)
#     calories += int(current_item[2])
#
# number_of_days = int(calories / 2000)
#
# print(f"You have food to last you for: {number_of_days} days!")
#
# for data in items:
#     products = data[0]
#     date = data[1]
#     current_calories = data[2]
#     print(f"Item: {products}, Best before: {date}, Nutrition: {current_calories}")




import re

text = input()

pattern = "#[A-Za-z\ ]+#\d{2}/\d{2}/\d{2}#\d{1,}#|\|[A-Za-z\ ]+\|\d{2}/\d{2}/\d{2}\|\d{1,}\|"

matches = re.findall(pattern, text)

calories = 0
for match in matches:
    if "#" in match:
        first = match.split("#")
        calories += int(first[3])
    elif "|" in match:
        second = match.split("|")
        calories += int(second[3])

per_day_nutrition = calories // 2000
print(f"You have food to last you for: {per_day_nutrition} days!")

for match in matches:
    if "#" in match:
        item = match.split("#")
        food = item[1]
        date = item[2]
        calorie = item[3]
        print(f"Item: {food}, Best before: {date}, Nutrition: {calorie}")
    elif "|" in match:
        item = match.split("|")
        food = item[1]
        date = item[2]
        calorie = item[3]
        print(f"Item: {food}, Best before: {date}, Nutrition: {calorie}")