from collections import deque


males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches_count = 0

while males and females:
    last_male = males[-1]
    first_female = females[0]

    if last_male <= 0 or first_female <= 0:
        if last_male <= 0:
            males.pop()
        else:
            females.popleft()

    elif last_male % 25 == 0 or first_female % 25 == 0:
        if last_male % 25 == 0:
            males.pop()
            males.pop()
        else:
            females.popleft()
            females.popleft()

    elif last_male == first_female:
        males.pop()
        females.popleft()
        matches_count += 1

    else:
        males[-1] -= 2
        females.popleft()

print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {', '.join([str(x) for x in males][::-1])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")