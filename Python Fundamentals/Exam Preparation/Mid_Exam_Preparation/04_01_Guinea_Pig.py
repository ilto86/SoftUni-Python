# food = float(input()) * 1000
# hay = float(input()) * 1000
# cover = float(input()) * 1000
# weight = float(input()) * 1000
# is_over = False
# counter = 0
#
# while counter < 30:
#     counter += 1
#     if counter % 1 == 0:
#         food -= 300
#     if counter % 2 == 0:
#         hay -= food * 0.05
#     if counter % 3 == 0:
#         cover -= weight / 3
#     if food <= 0 or hay <= 0 or cover <= 0:
#         is_over = True
#         break
#
# if is_over:
#     print("Merry must go to the pet store!")
# else:
#     print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")





food_quantity =  float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
guinea_pig_weigh = float(input()) * 1000
is_not_enough = False

for day in range(1, 31):
    food_quantity -= 300

    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        is_not_enough = True
        break

    if day % 2 == 0:
       hay_quantity -= food_quantity * 0.05

    if day % 3 == 0:
        cover_quantity -= guinea_pig_weigh / 3

if is_not_enough:
    print("Merry must go to the pet store!")
else:
    food_quantity /= 1000
    hay_quantity /= 1000
    cover_quantity /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")