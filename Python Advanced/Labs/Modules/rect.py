from line import print_line


def print_rect(width, height):
    for _ in range(height):
        print_line(width)

print(print_rect(5, 2))
print(print_rect(5, 3))
print(print_rect(5, 4))
print(print_rect(5, 5))