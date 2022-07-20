'''
First Solution
'''

current_year = int(input())
while True:
    current_year += 1
    current_year_as_string = str(current_year)
    happy_year = True
    for test_position in range(len(current_year_as_string)):
        test_digit = current_year_as_string[test_position]
        for current_position in range(len(current_year_as_string)):
            if test_digit == current_year_as_string[current_position] and not test_position == current_position:
                happy_year = False
                break
    if happy_year: # if happy_year == True:
        print(current_year)
        break



'''
Second Solution
'''

# current_year = int(input())
# while True:
#     current_year += 1
#     current_year_as_string = str(current_year)
#     if len(current_year_as_string) == len(set(current_year_as_string)):
#         print(current_year)
#         break


'''
Third Solution
'''

# year = int(input())
#
# while True:
#     year += 1
#     if len(str(year)) == len(set(str(year))):
#         print(year)
#         break


'''
Fourth Solution
'''

# number = int(input()) + 1
#
# while True:
#     year = str(number)
#     if len(set(year)) == len(year):
#         print(year)
#         break
#     number += 1
# year = int(input()) + 1
# while not len(set(str(year))) == len(str(year)):
#     year += 1
# print(year)


'''
Fifth Solution
'''

# random_number = int(input()) + 1
#
# for i in range(0, len(str(random_number))):
#     cheker = str(random_number).count(str(random_number)[i])
#
#     while cheker > 1:
#         random_number += 1
#         cheker = str(random_number).count(str(random_number)[i])
#
# print(random_number)
