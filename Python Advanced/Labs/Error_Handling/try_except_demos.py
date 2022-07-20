import random


def try_raise_exception():
    chance = 0.7
    if random.random() < chance:
        raise ValueError('Invalid value')


for i in range(100):
    try:
        # This code **MAY** raise an exception
        try_raise_exception()
        print(f'Try {i}: No exception')
    # `except` is `catch` in `C#`, `Java`, `Js`, etc...
    except ValueError:
        print(f'Try {i}: Value exception!')

try:
    x = sum(range(1, 15))
except:
    pass




# import random
#
#
# def try_raise_exception():
#     chance = 0.7
#     if random.random() < chance:
#         raise ValueError('Invalid value')
#
# for i in range(100):
#     try:
#         # This code **MAY** raise an exception
#         try_raise_exception()
#         print(f'Try {i}: No exception')
#     # 'except' is 'catch' in 'C#', 'Java', 'Js', etc...
#     except ValueError:
#         print(f'Try {i}: Value error handled!')
#     finally:
#         print(f'Try {i}: This is finally')






# def try_raise_exception():
#     chance = 0.3
#     value = random.random()
#     if value < chance:
#         raise ValueError('Invalid value')
#     elif value < 0.7:
#         raise TypeError('Invalid type')
#
#
# for i in range(10):
#     try:
#         try_raise_exception()
#         print(f'Try {i}: No exception')
#     except (ValueError, TypeError) as e:
#         print(f'Try {i}: Yes exception ({type(e).__name__}: {e})')
#
#
# for i in range(10):
#     try:
#         try_raise_exception()
#         print(f'Try {i}: No exception')
#     except ValueError as e:
#         print(f'Try {i}: Value exception ({type(e).__name__}: {e})')
#     except TypeError as e:
#         print(f'Try {i}: Type exception ({type(e).__name__}: {e})')


# try:
#     # raise ValueError
#     raise TypeError
# except ValueError:
#     print('Value exception')
# except Exception:
#     print('Base Exception')
# except:
#     print('Exception')






# def read_until_int():
#     while True:
#         try:
#             return int(input())
#         except ValueError:
#             print('Not an integer. Try again!')
#
# print(
#     read_until_int()
# )