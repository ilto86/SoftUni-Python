n = int(input())

positive_nums = []
negative_nums = []

for _ in range(n):
    current_num = int(input())
    if current_num >= 0:
        positive_nums.append(current_num)
    else:
        negative_nums.append(current_num)

print(positive_nums)
print(negative_nums)
print(f"Count of positives: {len(positive_nums)}")
print(f" Sum of negatives: {sum(negative_nums)}")