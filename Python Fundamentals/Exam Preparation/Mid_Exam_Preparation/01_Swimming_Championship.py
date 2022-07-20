# ILTO's Code

# days = int(input())
# points = int(input())
# count = int(input())
# room_price = float(input())
# participation_fee = float(input()) * count
#
# price_hotel = 0
# total_points = 0
# current_points = 0
# for day in range(1, days + 1):
#     points_earned = float(input())
#     price_hotel += count * room_price
#     if day == 1:
#         total_points += points_earned
#         current_points = points_earned
#     elif day != 1:
#         additional_points = 0.05 * current_points
#         current_points = 0
#         current_points += points_earned + additional_points
#         total_points += current_points
#
# if total_points >= points:
#     total_fee = price_hotel + participation_fee
#     sponsor_cover = total_fee * 0.25
#     money = total_fee - sponsor_cover
#     print(f"Money left to pay: {money:.2f} BGN.")
#     print("The championship was successful!")
# else:
#     total_fee = price_hotel + participation_fee
#     sponsor_cover = total_fee * 0.10
#     money = total_fee - sponsor_cover
#     print(f"Money left to pay: {money:.2f} BGN.")
#     print("The championship was not successful.")




# Sashko Code
days = int(input())
points = int(input())
count = int(input())
room_price = float(input())
participation_fee = float(input())

total_fee = participation_fee * count
current_points = 0
total_points = 0

for day in range(1, days + 1):
    points_earned = float(input())

    if day > 1:
        points_earned += current_points * 0.05

    total_fee += room_price * count
    current_points = points_earned
    total_points += points_earned

if total_points >= points:
    total_fee -= total_fee * 0.25
    print(f"Money left to pay: {total_fee:.2f}")
    print("The championship was successful!")
else:
    total_fee -= total_fee * 0.10
    print(f"Money left to pay: {total_fee:.2f}")
    print("The championship was not successful.")






# Sashko Code
# days_of_championship = int(input())
# points_needed = int(input())
# swimmers_count = int(input())
#
# hotel_room_price_per_day = float(input())
# tax_per_swimmer = float(input())
#
# total_expenses = tax_per_swimmer * swimmers_count
# total_points = 0
#
# last_day_points = 0
#
# for day in range(1, days_of_championship + 1):
#     points_earned_for_day = float(input())
#     if day > 1:
#         points_earned_for_day += last_day_points * 0.05
#
#     total_points += points_earned_for_day
#     last_day_points = points_earned_for_day
#
#     total_expenses += hotel_room_price_per_day * swimmers_count
#
# if total_points >= points_needed:
#     total_expenses -= total_expenses * 0.25
#     print(f"Money left to pay: {total_expenses:.2f}")
#     print("The championship was successful!")
# else:
#     total_expenses -= total_expenses * 0.10
#     print(f"Money left to pay: {total_expenses:.2f}")
#     print("The championship was not successful.")
