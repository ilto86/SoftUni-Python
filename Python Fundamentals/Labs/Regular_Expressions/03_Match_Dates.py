# import re
#
# text= input()
#
# expression = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
#
# matches = re.finditer(expression, text)
#
# for match in matches:
#     day = match.group("day")
#     month = match.group("month")
#     year = match.group("year")
#
#     print(f"Day: {day}, Month: {month}, Year: {year}")
#
#
#
#
#
# pattern = r"(?P<Day>\d{2})(?P<separator>[-/\.])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"
# text = input()
#
# valid_dates = re.finditer(pattern, text)
# for date in valid_dates:
#     current_date = date.groupdict()
#     print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}")





import re

pattern = r"\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
text = input()
matches = re.findall(pattern, text)

for match in matches:
    day, month, year = match[0], match[2], match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")