# -----------------------------------------------------------  Functions Returning Functions  -----------------------------------------------------------


# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
#
#
# hello = hello_function()
# hello()
# print(hello())


# message = "from Global Scope"
# def print_message(message):
#     print("from outter function <----> from Local scope")
#
#     def message_sender():
#         "Nested Function"
#         print("from inner function <----> from Enclosing scope")
#         print(message)
#     message_sender()
#
#
# print_message("I give from Global scope into function <----> this Message")
# print("\n")
# print("=" * 20)
# print("\n")
# print(message)



# -----------------------------------------------------------  Decorators  -----------------------------------------------------------



# def uppercase(function):
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#     return wrapper
#
#
# '''is the grotesque way'''
# def say_hi():
#     return 'hello there'
#
# decorate = uppercase(say_hi)
# decorate()
#
#
# '''is the proper way'''
# @uppercase
# def say_hi():
#  return 'hello there'
# print(say_hi()) # HELLO THERE

# -----------------------------------------------------------  Passing Arguments with *args and **kwargs  -----------------------------------------------------------



from symbol import decorator


# def repeat(n):
#     def decorator(function):
#         def wrapper():
#             for _ in range(n):
#                 function()
#         return wrapper
#     return decorator
#
# # This is Better Deco:
# @repeat(4)
# def say_hi():
#     print("I want to say Hello 4 times")
# say_hi()
#
#
# # This is not good Deco:
# def say_hi():
#     print("I want to say Hello 4 times")
#
# repeat(4)(say_hi)()
# # so is little better than top one:
# decorated = repeat(4)
# main_purpose = decorated(say_hi)
# main_purpose()


# -----------------------------------------------------------  Accepting Arguments with *args and **kwargs  -----------------------------------------------------------



# from time import time, sleep
#
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print(end - start)
#         return result
#     return wrapper
#
#
# @measure_time
# def even_array(nums):
#     sleep(4)
#     return [n for n in nums if n % 2 == 0]
#
# print(even_array([101, 202, 303, 404, 505, 606, 707, 808, 909, 1001]))



# -----------------------------------------------------------  Classes as Decorators  -----------------------------------------------------------

# class Fibonacci:
#     def __init__(self):
#         self.cache = {}
#
#     def __call__(self, n):
#         if n not in self.cache:
#             if n == 0:
#                 self.cache[0] = 0
#             elif n == 1:
#                 self.cache[1] = 1
#             else:
#                 self.cache[n] = self(n-1) + self(n-2)
#         return self.cache[n]
#
#
# fib = Fibonacci()
#
# for i in range(5):
#     print(fib(i))
#
# print(fib.cache)






# class func_logger:
#     _logfile = 'out.log'
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args):
#         log_string = self.func.__name__ + " was called"
#         with open(self._logfile, 'a') as opened_file:
#             opened_file.write(log_string + '\n')
#         return self.func(*args)
#
#
# @func_logger
# def say_hi(name):
#     print(f"Hi, {name}")
#
# @func_logger
# def say_bye(name):
#     print(f"Bye, {name}")
#
# say_hi("Peter")
# say_bye("Peter")