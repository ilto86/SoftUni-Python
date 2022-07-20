from collections import deque


def best_list_pureness(numbers, n):
    count = n
    numbers_queue = deque(numbers)
    rotate_numbers = []
    for i in range(count + 1):
        numbers_sum = 0
        for idx, el in enumerate(numbers_queue):
            numbers_sum += el * idx

        numbers_queue.rotate(1)  # rotated forward (to right)
        rotate_numbers.append(numbers_sum)

    best_count = rotate_numbers.index(max(rotate_numbers))
    highest_pureness = max(rotate_numbers)

    return f"Best pureness {highest_pureness} after {best_count} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)                       # Best pureness 26 after 3 rotations


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)                       # Best pureness 78 after 2 rotations


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)                       # Best pureness 40 after 0 rotations