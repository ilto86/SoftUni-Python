biscuits_produced_per_worker_per_day = int(input())
count_of_workers = int(input())
number_of_biscuits = int(input())
every_third_day = 0
count_biscuits = 0

for i in range(1, 31):
    every_day_produce = biscuits_produced_per_worker_per_day * count_of_workers
    if i % 3 == 0:
        every_third_day = every_day_produce * 0.75
        count_biscuits += int(every_third_day)
    else:
        count_biscuits += int(every_day_produce)

difference = abs(count_biscuits - number_of_biscuits)
diff_in_percent = difference / number_of_biscuits * 100
print(f"You have produced {count_biscuits} biscuits for the past month.")
if count_biscuits > number_of_biscuits:
    print(f"You produce {diff_in_percent:.2f} percent more biscuits.")
else:
    print(f"You produce {diff_in_percent:.2f} percent less biscuits.")

