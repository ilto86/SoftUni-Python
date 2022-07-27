from time import time


def exec_time(func_ref):
    def wrapper(*args):
        # start stopwatch
        start = time()

        # execution the function
        func_ref(*args)

        # end stopwatch
        end = time()

        # return elapsed time
        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


# print(concatenate(["a" for i in range(1000000)]))


@exec_time
def loop():
    count = 0
    for i in range(1, 10000000):
        count += 1


print(loop())




''' log in txt file '''
# from time import time
#
#
# def exec_time(func_ref):
#     def wrapper(*args):
#         # start stopwatch
#         start = time()
#
#         # execution the function
#         result = func_ref(*args)
#
#         # end stopwatch
#         end = time()
#
#         with open("./results.txt", "a") as file:
#             file.write(f"{func_ref.__name__} was called with {args}. Elapsed: {end - start}")
#         # return elapsed time
#         return result
#
#     return wrapper
#
#
# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x