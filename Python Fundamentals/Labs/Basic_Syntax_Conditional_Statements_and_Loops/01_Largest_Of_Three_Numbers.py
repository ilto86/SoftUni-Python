# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
# print(max(num_1, num_2, num_3))



first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)

