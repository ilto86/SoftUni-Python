numbers_string = input()

occurences_counts = {}
numbers = [float(x) for x in numbers_string.split()]

for number in numbers:
    if number not in occurences_counts:
        occurences_counts[number] = 0
    occurences_counts[number] += 1

for number, count in occurences_counts.items():
    print(f"{number:.1f} - {count} times")




# nums = tuple(float(el) for el in input().split())
# occurences = {}
#
# for num in nums:
#     occurences[num] = nums.count(num)
#
# for kvp in occurences.items():
#     print(f"{kvp[0]} - {kvp[1]} times")






# nums = (float(el) for el in input().split())
#
# occurences = {}
#
# for num in nums:
#     if num not in occurences:
#         occurences[num] = 0
#     occurences[num] += 1
#
# for kvp in occurences.items():  # for key,value in occurences.items():
#     print(f"{kvp[0]} - {kvp[1]} times") #     print(f"{key} - {value} times")






# numbers = tuple(map(float, input().split()))
#
# nums_and_occurances = {}
# for num in numbers:
#     if num not in nums_and_occurances:
#         nums_and_occurances[num] = 0
#     nums_and_occurances[num] += 1
#
# [print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]



# numbers = list(map(float, input().split()))
#
# nums_and_occurances = {}
# for num in numbers:
#     if num not in nums_and_occurances:
#         nums_and_occurances[num] = 0
#     nums_and_occurances[num] += 1
#
# [print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]