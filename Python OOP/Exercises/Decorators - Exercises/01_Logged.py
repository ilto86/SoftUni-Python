def logged(func_ref):
    def wrapper(*args):
        func_name = func_ref.__name__
        func_result = func_ref(*args)
        return f"you called {func_name}{args}\nit returned {func_result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))

print(sum_func(1, 4))