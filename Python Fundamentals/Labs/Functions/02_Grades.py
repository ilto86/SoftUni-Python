# grade_data = float(input())
#
# def solve(grade):
#     if 2.00 <= grade <= 2.99:
#         return 'Fail'
#     elif 3.00 <= grade <= 3.49:
#         return 'Poor'
#     elif 3.50 <= grade <= 4.49:
#         return 'Good'
#     elif 4.50 <= grade <= 5.49:
#         return 'Very Good'
#     elif 5.50 <= grade <= 6.00:
#         return 'Excellent'
# print(solve(grade_data))



# def grade_text():
#     grade_number = float(input())
#
#     if 2.00 <= grade_number <= 2.99:
#         return 'Fail'
#     elif 3.00 <= grade_number <= 3.49:
#         return 'Poor'
#     elif 3.50 <= grade_number <= 4.49:
#         return 'Good'
#     elif 4.50 <= grade_number <= 5.49:
#         return 'Very Good'
#     elif 5.50 <= grade_number <= 6.00:
#         return 'Excellent'
#
# print(grade_text())



# def grade_text(grade_number):
#
#     if 2.00 <= grade_number <= 2.99:
#         return 'Fail'
#     elif 3.00 <= grade_number <= 3.49:
#         return 'Poor'
#     elif 3.50 <= grade_number <= 4.49:
#         return 'Good'
#     elif 4.50 <= grade_number <= 5.49:
#         return 'Very Good'
#     elif 5.50 <= grade_number <= 6.00:
#         return 'Excellent'
#
# current_grade = float(input())
#
# print(grade_text(current_grade))

# print(grade_text(5))




# def grade_to_text(grade):
#
#     if 2.00 <= grade <= 2.99:
#         print("Fail")
#     elif 3.00 <= grade <= 3.49:
#         print("Poor")
#     elif 3.50 <= grade <= 4.49:
#         print("Good")
#     elif 4.50 <= grade <= 5.49:
#         print("Very Good")
#     elif 5.50 <= grade <= 6.00:
#         print("Excellent")
#
# grade_as_num = float(input())
# grade_to_text(grade_as_num)




def grade_to_text(grade):

    if 2.00 <= grade <= 2.99:
        return ("Fail")
    elif 3.00 <= grade <= 3.49:
        return ("Poor")
    elif 3.50 <= grade <= 4.49:
        return ("Good")
    elif 4.50 <= grade <= 5.49:
        return ("Very Good")
    elif 5.50 <= grade <= 6.00:
        return ("Excellent")

grade_as_num = float(input())
print(grade_to_text(grade_as_num))