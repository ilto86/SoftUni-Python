n = int(input())

opening_braxkets_count = 0
closing_braxkets_count = 0
is_balanced = True

for i in range(n):
    text = input()
    if text == "(":
        opening_braxkets_count += 1
    elif text == ")":
        closing_braxkets_count += 1

    if closing_braxkets_count > opening_braxkets_count:
        is_balanced = False
        break
    elif opening_braxkets_count - 1 > closing_braxkets_count:
        is_balanced = False
        break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")