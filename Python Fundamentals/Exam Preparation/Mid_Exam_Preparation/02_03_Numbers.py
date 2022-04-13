# numbers = [int(num) for num in input().split()]
# result = sum(numbers)
# avarage = result/ len(numbers)
# avarage_5 = list()
#
# for i in numbers:
#     if i > avarage:
#         avarage_5.append(i)
#
# avarage_5.sort(reverse=True)
# if len(avarage_5) > 5:
#         avarage_5 = avarage_5[:5]
# if len(avarage_5) > 0:
#         output = [str(el) for el in avarage_5]
#         print(" ".join(output))
# else:
#     print("No")




# numbers = [int(num) for num in input().split()]
# result = sum(numbers)
# avarage = result/ len(numbers)
# avarage_5 = [num for num in numbers if num > avarage]
#
# avarage_5.sort(reverse=True)
#
# if len(avarage_5) > 5:
#         avarage_5 = avarage_5[:5]
# if len(avarage_5) > 0:
#         output = [str(el) for el in avarage_5]
#         print(" ".join(output))
# else:
#     print("No")



# numbers = [int(el) for el in input().split()]
#
# greater_than_average = [n for n in numbers if n > sum(numbers) / len(numbers)]
#
# greater_than_average.sort(reverse=True)
#
# if len(greater_than_average) == 0:
#     print("No")
#
# elif len(greater_than_average) < 6:
#     greater_than_average = [str(n) for n in greater_than_average]
#     print(" ".join(greater_than_average))
#
# else:
#     greater_than_average = [str(n) for n in greater_than_average]
#     print(" ".join(greater_than_average[:5]))


numbers = [int(num) for num in input().split()]
avarage = sum(numbers) / len(numbers)
avarage_numbers = [num for num in numbers if num > avarage]
avarage_numbers.sort(reverse=True)
top_five = []
count = 5

for top_num in avarage_numbers:
    if count == 0:
        break
    else:
        top_five.append(top_num)
        count -= 1

if len(avarage_numbers) > 0:
    avarage_numbers = [str(num) for num in top_five]
    print(" ".join(avarage_numbers))
else:
    print("No")