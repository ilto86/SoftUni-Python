from collections import deque

# green_light_in_seconds = int(input())
# free_window_in_seconds = int(input())
# command = input()
# cars = deque()
# passed = 0
# crash = False
#
# while command != "END":
#     if crash:
#         break
#
#     if command != "green":
#         cars.append(command)
#
#     elif command == "green":
#         time = green_light_in_seconds
#         extra_time = free_window_in_seconds
#
#         while time > 0:
#             if cars:
#                 current_car = cars.popleft()
#                 crashed_car = current_car
#             else:
#                 break
#
#             for i in range(len(current_car)):
#                 current_car = list(current_car)
#                 char = current_car.pop(0)
#                 if len(current_car) == 0:
#                     passed += 1
#                 time -= 1
#                 if time < 0:
#                     extra_time -= 1
#                     if extra_time < 0:
#                         print("A crash happened!")
#                         print(f"{crashed_car} was hit at {char}.")
#                         crash = True
#                         break
#     command = input()
#
# if not crash:
#     print(f"Everyone is safe.")
#     print(f"{passed} total cars passed the crossroads.")












green_light = int(input())
free_window = int(input())

cars = deque()
passed_counter = 0
crashed = False

while not crashed:
    line = input()
    if line == "END":
        break

    if line == "green":
        current_green = green_light
        while cars and current_green > 0:
            car = cars.popleft()
            if len(car) <= current_green + free_window:
                passed_counter += 1
            else:
                print("A crash happened!")
                print(f"{car} was hit at {car[current_green + free_window]}")
                crashed = True
                break
            current_green -= len(car)
    else:
        cars.append(line)

if not crashed:
    print("Everyone is safe.")
    print(f"{passed_counter} total cars passed the crossroads.")