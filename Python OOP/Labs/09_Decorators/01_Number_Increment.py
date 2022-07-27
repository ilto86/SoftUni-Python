def number_increment(numbers):
    def increase():
        increased = [num + 1 for num in numbers]
        return increased
    return increase()


print(number_increment([0, 1, 2]))
print(number_increment([3, 4, 5]))
print(number_increment([6, 7, 8]))