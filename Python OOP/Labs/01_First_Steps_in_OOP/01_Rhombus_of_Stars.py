'''
n = 3
  *         # i = 0, 2 spaces (n - 1 - i spaces), 1 star
 * *        # i = 1, 1 spaces (n - 1 - i spaces), 1 star, 1 space, 1 star
* * *       # i = 2, 0 spaces, 1 star, 1 space, 1 star, 1 space
 * *
  *
n = 4
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
'''


def get_line(i, n, char='*'):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + (f'{char} ' * stars_count).strip()


def get_rhombus(n):
    return [get_line(i, n) for i in range(n)] + \
           [get_line(i, n) for i in range(n - 2, -1, -1)]


def print_line(n):
    print(get_line(n - 1, n - 1))


def print_square(n):
    [print(get_line(n - 1, n - 1, '@')) for _ in range(n)]


def print_rhombus(n):
    [print(row) for row in get_rhombus(n)]


print_rhombus(3)
print_rhombus(4)
print_line(4)
print_square(5)









# def print_row(n, row):
#     for space in range(n - row):
#         print(" ", end="")
#     for star in range(1, row):
#         print("*", end=' ')
#     print("*")
#
#
# def print_up(n):
#     for row in range(1, n + 1):
#         print_row(n, row)
#
#
# def print_bottom(n):
#     for row in range(n - 1, 0, -1):
#         print_row(n, row)
#
#
# def print_rhombus(n):
#     print_up(n)
#     print_bottom(n)
#
#
# n = int(input())
# print_rhombus(n)




# n = int(input())
# # print_rhombus(n)
#
# for row in range(1, n + 1):
#     for space in range(n - row):
#         print(" ", end="")
#     for star in range(1, row):
#         print("*", end=' ')
#     print("*")
#
# for row in range(n - 1, 0, -1):
#     for space in range(n - row):
#         print(" ", end="")
#     for star in range(1, row):
#         print("*", end=' ')
#     print("*")