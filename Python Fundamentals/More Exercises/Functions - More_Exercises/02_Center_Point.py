# from math import floor
#
# def point_closest_to_center(X1, Y1, X2, Y2):
#     distance_1 = X1 ** 2+Y1 ** 2
#     distance_2 = X2 ** 2+Y2 ** 2
#     if distance_1 <= distance_2:
#         hit_1 = (floor(int(X1)), floor(int(Y1)))
#         return hit_1
#     else:
#         hit_2 = (floor(int(X2)), floor(int(Y2)))
#         return hit_2
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# print(point_closest_to_center(x1, y1, x2, y2))



# from math import sqrt
#
#
# def calculate_distance_from_center(x, y):
# 	d = sqrt((x ** 2) + (y ** 2))
# 	return d
#
#
# def check_closest_point(point1, point2):
# 	x1, y1 = point1
# 	x2, y2 = point2
# 	distance_1 = calculate_distance_from_center(x1, y1)
# 	distance_2 = calculate_distance_from_center(x2, y2)
# 	if distance_1 <= distance_2:
# 		point1 = int(x1), int(y1)
# 		return point1
# 	else:
# 		point2 = int(x2), int(y2)
# 		return point2
#
#
# first_point = (float(input()), float(input()))
# second_point = (float(input()), float(input()))
#
# print(check_closest_point(first_point, second_point))



import math

def closest():

    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    diff_x1_y1 = abs(x1) + abs(y1)
    diff_x2_y2 = abs(x2) + abs(y2)

    if diff_x1_y1 < diff_x2_y2:
        print(f'({math.floor(int(x1))}, {math.floor(int(y1))})')

    elif diff_x2_y2 < diff_x1_y1:
        print(f'({math.floor(int(x2))}, {math.floor(int(y2))})')

    else:
        print(f'({math.floor(int(x1))}, {math.floor(int(y1))})')

closest()