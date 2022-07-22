'''
First Solution
'''


# class dictionary_iter:
#     def __init__(self, object):
#         self.object = list(object.items())
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx >= len(self.object):
#             raise StopIteration
#         current_pair = self.object[self.idx]
#         self.idx += 1
#         return current_pair



'''
Second Solution
'''


class dictionary_iter:
    def __init__(self, object):
        self.object = object
        self.generator = (pair for pair in self.object.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)