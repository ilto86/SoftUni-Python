from itertools import combinations

seq = [1,2,3,4]
for first, second in combinations(seq, 2):
    print(first, second)

from itertools import combinations

sequence = [int(el) for el in input().split()]
target = int(input())

my_set = set()
iterations = 0

for num in combinations(sequence, 2):
    if num[0] + num[1] == target:
        iterations += 1
        my_set.add((num[0], num[1]))
        print(f"{num[0]} + {num[1]} = {target}")
    else:
        iterations += 1

print(f"Iterations done: {iterations}")
if my_set:
    print(*my_set, sep="\n")