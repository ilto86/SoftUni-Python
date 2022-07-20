n = int(input())
cars = set()

for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")







# n = int(input())
#
# parkink_lot_logs = [input().split(", ") for _ in range(n)]
#
# parking_lot = set()
#
# for direction, car_number in parkink_lot_logs:
#     if direction == "IN":
#         parking_lot.add(car_number)
#     else:
#         parking_lot.remove(car_number)
#
# if parking_lot:
#     [print(car_number) for car_number in parking_lot]
# else:
#     print("Parking Lot is Empty")