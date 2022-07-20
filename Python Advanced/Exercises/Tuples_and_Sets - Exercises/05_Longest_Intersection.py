n = int(input())
best_intersection = set()

for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = [int(x) for x in first_range.split(",")]
    second_start, second_end = [int(x) for x in second_range.split(",")]

    first = set(range(first_start, first_end + 1))
    second = set(range(second_start, second_end + 1))

    current_intsection = first.intersection(second)
    if len(current_intsection) > len(best_intersection):
        best_intersection = current_intsection

print(f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}] with length {len(best_intersection)}")





# n = int(input())
# numbers_set_1 = set()
# numbers_set_2 = set()
# longest_intersection = set()
# for _ in range(n):
#     first_range, second_range = input().split("-")
#     start_idx_1, stop_idx_1 = [int(el) for el in first_range.split(",")]
#     start_idx_2, stop_idx_2 = [int(el) for el in second_range.split(",")]
#
#     for num in range(start_idx_1, stop_idx_1 + 1):
#         numbers_set_1.add(num)
#     for num in range(start_idx_2, stop_idx_2 + 1):
#         numbers_set_2.add(num)
#
#     intersection = numbers_set_1 & numbers_set_2
#     numbers_set_1.clear()
#     numbers_set_2.clear()
#
#     if not longest_intersection or len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")
