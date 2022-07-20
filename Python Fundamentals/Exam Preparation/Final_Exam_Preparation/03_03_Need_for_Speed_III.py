# number_of_cars = int(input())
# cars_dict = dict()
#
# for _ in range(number_of_cars):
#     cars = input().split("|")
#     car = cars[0]
#     mileage = int(cars[1])
#     fuel = int(cars[2])
#     if car not in cars_dict:
#         cars_dict[car] = {"Mileage": mileage, "Fuel": fuel}
#
# while True:
#     commands = input()
#     if commands == "Stop":
#         break
#
#     command = commands.split(' : ')
#
#     if command[0] == "Drive":
#      car = command[1]
#      distance = int(command[2])
#      fuel = int(command[3])
#      if fuel < cars_dict[car]["Fuel"]:
#          cars_dict[car]["Mileage"] += distance
#          cars_dict[car]["Fuel"] -= fuel
#          print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#          if cars_dict[car]["Mileage"] > 99999:
#             del cars_dict[car]
#             print(f"Time to sell the {car}!")
#      else:
#          print("Not enough fuel to make that ride")
#          if cars_dict[car]["Mileage"] > 99999:
#             del cars_dict[car]
#             print(f"Time to sell the {car}!")
#
#     elif command[0] == "Refuel":
#      car = command[1]
#      fuel = int(command[2])
#      if cars_dict[car]["Fuel"] + fuel > 75:
#          fuel = 75 - cars_dict[car]["Fuel"]
#          cars_dict[car]["Fuel"] = 75
#      else:
#          cars_dict[car]["Fuel"] += fuel
#
#      print(f"{car} refueled with {fuel} liters")
#
#     elif command[0] == "Revert":
#         car = command[1]
#         kilometers = int(command[2])
#         if cars_dict[car]["Mileage"] - kilometers > 10000:
#             cars_dict[car]["Mileage"] -= kilometers
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#         else:
#             cars_dict[car]["Mileage"] = 10000
#
# for vechile in cars_dict:
#     print(f"{vechile} -> Mileage: {cars_dict[vechile]['Mileage']} kms, Fuel in the tank: {cars_dict[vechile]['Fuel']} lt.")






number_of_cars = int(input())

cars = {}
for _ in range(number_of_cars):
    data = input().split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    cars[car] = {"Mileage": mileage, "Fuel": fuel}

while True:
    commands = input()
    if commands == "Stop":
        break

    order = commands.split(" : ")
    command = order[0]
    car = order[1]

    if command == "Drive":
        distance = int(order[2])
        fuel = int(order[3])
        if cars[car]["Fuel"] < fuel:
            print("Not enough fuel to make that ride")
        if cars[car]["Fuel"] >= fuel:
            cars[car]["Mileage"] += distance
            cars[car]["Fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["Mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    if command == "Refuel":
        fuel = int(order[2])
        if fuel + cars[car]["Fuel"] > 75:
            required_fuel = 75 - cars[car]["Fuel"]
            print(f"{car} refueled with {required_fuel} liters")
            cars[car]["Fuel"] = 75
        else:
            cars[car]["Fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    if command == "Revert":
        amount_reverted = int(order[2])
        if cars[car]["Mileage"] - amount_reverted <= 10000:
            cars[car]["Mileage"] = 10000
        else:
            cars[car]["Mileage"] -= amount_reverted
            print(f"{car} mileage decreased by {amount_reverted} kilometers")

for car, km in cars.items():
    mileage = km["Mileage"]
    fuel = km["Fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")