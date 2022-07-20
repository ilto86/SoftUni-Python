# from collections import deque
#
# count = int(input())
# gas_station = deque()
#
# for _ in range(count):
#     data = [int(x) for x in input().split()]
#     gas_station.append(data)
#
# for index in range(len(gas_station)):
#     tank = 0
#     failed = False
#
#     for fuel, distance in gas_station:
#         tank += fuel
#
#         if distance > tank:
#             failed = True
#             break
#         else:
#             tank -= distance
#
#     if failed:
#         gas_station.append(gas_station.popleft())    # pump_station.rotate(-1)
#     else:
#         print(index)
#         break



from collections import deque

pumps_count = int(input())
pumps = deque()

for _ in range(pumps_count):
    pumps.append([int(x) for x in input().split()])

for attempt in range(pumps_count):
    trunk = 0
    failed = False
    for petrol, distance in pumps:
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())    # pump_station.rotate(-1)
    else:
        print(attempt)
        break