'''
First Solution
'''


# class sequence_repeat:
#     def __init__(self, sequence, number):
#         self.sequence = sequence
#         self.number = number
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.number:
#             string_length = len(self.sequence) - 1
#             if self.idx > string_length:
#                 self.idx = 0
#
#             current_string = self.sequence[self.idx]
#             self.idx += 1
#             self.number -= 1
#             return current_string
#         else:
#             raise StopIteration()



'''
Second Solution
'''


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer == self.number:
            raise StopIteration()
        symbol = self.sequence[self.pointer % len(self.sequence)]
        self.pointer += 1
        return symbol

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')