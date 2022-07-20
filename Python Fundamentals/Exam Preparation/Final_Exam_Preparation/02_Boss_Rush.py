import re

number = int(input())

for num in range(number):
    text = input()

    pattern = r"\|[A-Z]+\|\:#[A-Za-z]+\s[A-Za-z]+#"

    matches = re.findall(pattern, text)

    if matches:
        string = "".join(matches)
        boss = string.split("|")
        boss_name = boss[1]
        token = string.split("#")
        title = token[1]
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")

    else:
        print("Access denied!")

