from collections import deque

numbers_of_clock_cycles = deque([int(x) for x in input().split(", ")])
index = int(input())
total_clock_cycles = 0
break_point_number = numbers_of_clock_cycles[index]

while numbers_of_clock_cycles:
    min_number = min(numbers_of_clock_cycles)
    idx = numbers_of_clock_cycles.index(min_number)

    if min_number == break_point_number and numbers_of_clock_cycles.count(min_number) < 2:
        total_clock_cycles += numbers_of_clock_cycles[idx]
        break

    if numbers_of_clock_cycles[0] != min_number:
        numbers_of_clock_cycles.append(numbers_of_clock_cycles.popleft())
    elif numbers_of_clock_cycles[0] == numbers_of_clock_cycles[idx]:
        total_clock_cycles += numbers_of_clock_cycles.popleft()

print(total_clock_cycles)
