class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        return (pair for pair in self.__dict__.items())
        # yield ('name', self.name)
        # yield ('age', self.age)
        # for pair in self.__dict__.items():
        #     yield pair


def deep_loop(ll):
    for value in ll:
        for x in value:
            yield x


doncho = Person('Mark', 19)

for x in doncho:
    print(x)

people = [
    Person('Mark', 19),
    Person('Larry', 9),
]

[print(x) for x in deep_loop(people)]