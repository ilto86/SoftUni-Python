# number_of_lines = int(input())
# water_tank = 255
# counter = 0
#
# for _ in range(number_of_lines):
#     receive_liters_of_water = int(input())
#     water_tank -= receive_liters_of_water
#     if receive_liters_of_water > water_tank and water_tank < 0:
#         water_tank += receive_liters_of_water
#         print("Insufficient capacity!")
#     else:
#         counter += receive_liters_of_water
#
# print(counter)



number_of_lines = int(input())
capacity = 0

for _ in range(number_of_lines):
    liters_of_water = int(input())

    if liters_of_water + capacity <= 255:
        capacity += liters_of_water
        continue

    print("Insufficient capacity!")

print(capacity)