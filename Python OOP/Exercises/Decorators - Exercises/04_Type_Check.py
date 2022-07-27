def type_check(type):
    def decorator(func_ref):
        def wrapper(argument):
            if isinstance(argument, type):
                return func_ref(argument)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


@type_check(str)
def first_letter(word):
    return word[0]


print(times2(2))
print(times2('Not A Number'))

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))