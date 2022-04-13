numbers = input().split(", ")
numbers = list(map(int, numbers))
even_index_numbers = list()

# even_indices_numbers = map(lambda num: , numbers)

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_index_numbers.append(i)

print(even_index_numbers)



# nums=[int(el) for el in input().split(", ")]
# print([index for index in range(len(nums)) if nums[index]%2==0])

# nums=[int(el) for el in input().split(", ")]
# print([index for index in range(len(nums)) if nums[index] % 2 == 0, int(el) for el in input().split(", ") ])