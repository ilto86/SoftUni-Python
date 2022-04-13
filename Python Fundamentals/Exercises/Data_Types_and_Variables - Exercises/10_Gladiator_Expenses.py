# lost_fights_count = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# expenses = 0
#
# for i in range(1, lost_fights_count + 1):
#     if i % 2 == 0:
#         expenses += helmet_price
#     if i % 3 == 0:
#         expenses += sword_price
#     if i % 6 == 0:
#         expenses += shield_price
#     if i % 12 == 0:
#         expenses += armor_price
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")


lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

gladiator_expenses = 0
shield_counter = 0

for lost in range(1, lost_fights_count + 1):

    if lost % 2 == 0:
        gladiator_expenses += helmet_price
    if lost % 3 == 0:
        gladiator_expenses += sword_price

        if lost % 2 == 0:
            gladiator_expenses += shield_price
            shield_counter += 1

            if shield_counter == 2:
                gladiator_expenses += armor_price
                shield_counter = 0

print(f"Gladiator expenses: {gladiator_expenses:.2f} aureus")