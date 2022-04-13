# First solution of the problem:

numbers = [int(el) for el in input().split()]

greater_than_average = [n for n in numbers if n > sum(numbers) / len(numbers)]

greater_than_average.sort(reverse=True)

if len(greater_than_average) == 0:
    print("No")

elif len(greater_than_average) < 6:
    greater_than_average = [str(n) for n in greater_than_average]
    print(" ".join(greater_than_average))

else:
    greater_than_average = [str(n) for n in greater_than_average]
    print(" ".join(greater_than_average[:5]))

    
 



# Second solution of the problem:

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
