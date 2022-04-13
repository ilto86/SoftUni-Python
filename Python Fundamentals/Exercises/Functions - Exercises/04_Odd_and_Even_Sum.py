# def odd_even_sum(nums):
#     odd_sum = 0
#     even_sum = 0
#     for num in nums:
#         if num % 2 == 0:
#             even_sum += num
#         else:
#             odd_sum += num
#
#     print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
#
#
# numbers = map(int, list(input()))
# odd_even_sum(numbers)


def get_even_and_odd_numbers(number):
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_numbers += int(digit)
        else:
            sum_of_odd_numbers += int(digit)

    return sum_of_even_numbers, sum_of_odd_numbers

number_as_string = input().split()
even_sum, odd_sum = get_even_and_odd_numbers(number_as_string)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")