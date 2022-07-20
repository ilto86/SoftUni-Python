# expression  = input()
# opening_brackets = []
# balanced = True
#
# for ch in expression:
#     if ch in "({[":
#         opening_brackets.append(ch)
#     elif not opening_brackets:
#         balanced = False
#         break
#     else:
#         last_opening_bracket = opening_brackets.pop()
#         if f"{last_opening_bracket}{ch}" not in "(){}[]":
#             balanced = False
#             break
#
# if balanced and not opening_brackets:
#     print("YES")
# else:
#     print("NO")







expression  = input()

opening_brackets = []

pairs = {
    "(": ")",
    "{": "}",
    "[": "]"
}

balanced = True

for ch in expression:
    if ch in "({[":
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False
            break

    if not balanced:
        break

if not balanced or opening_brackets:
    print("NO")
else:
    print("YES")