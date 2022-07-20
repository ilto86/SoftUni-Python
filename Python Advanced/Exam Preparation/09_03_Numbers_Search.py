def numbers_searching(*args):
    missing_number = []
    unique_numbers = set()
    max_number = max(args)
    min_number = min(args)
    for num in range(min_number, max_number + 1):
        if num not in args:
            missing_number.append(num)
    repeating_numbers = [x for x in args if args.count(x) > 1]
    unique_numbers = unique_numbers.union(repeating_numbers)
    missing_number.append(sorted([x for x in unique_numbers]))

    return missing_number


print(numbers_searching(1, 2, 4, 2, 5, 4))              # [3, [2, 4]]
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))     # [6, [5, 7, 9]]
print(numbers_searching(50, 50, 47, 47, 48, 45, 49,   # [46, [44, 45, 47, 48, 50]]
44, 47, 45, 44, 44, 48, 44, 48))