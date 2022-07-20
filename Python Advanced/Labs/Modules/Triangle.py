from line import print_line


def print_triangle(n):
    for i in range(n):
        print_line(i + 1)

    for i in range(n - 2, -1, -1):
        print_line(i + 1)


print_triangle(2)
print_triangle(3)
print_triangle(4)
print_triangle(5)
print_triangle(6)


'''
N = 3
1
1 2
1 2 3
1 2
1
N = 4
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
'''