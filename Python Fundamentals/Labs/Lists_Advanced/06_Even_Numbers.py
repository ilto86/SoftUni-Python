'''
First Solution with List Comprehension but this is not readable
'''
# print([index for index in range(len(nums)) if nums[index] % 2 == 0, int(el) for el in input().split(", ") ])

'''
Second Solution with List Comprehension this is more readable from first one
'''

# nums=[int(el) for el in input().split(", ")]
# print([index for index in range(len(nums)) if nums[index] % 2 == 0])


'''
Thirt Solution without List Comprehension and this is more readable than the other two
'''

numbers = input().split(", ")
numbers = list(map(int, numbers))
even_index_numbers = list()

# even_indices_numbers = map(lambda num: , numbers)

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_index_numbers.append(i)

print(even_index_numbers)
