class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.passed_iterations = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.passed_iterations == self.count:
            raise StopIteration()
        current_number = self.passed_iterations * self.step
        self.passed_iterations += 1
        return current_number


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)