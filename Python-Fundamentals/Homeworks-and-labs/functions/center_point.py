import math

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())


def determine_closest(x1, y1, x2, y2):

    if abs(x1) > abs(x2) and abs(y1) > abs(y2):
        point_x = x2
        point_y = y2
    else:
        point_x = x1
        point_y = y1

    if point_x > 0:
        if point_y > 0:
            print(f'({math.floor(point_x)}, {math.floor(point_y)})')
        else:
            print(f'({math.floor(point_x)}, -{math.floor(abs(point_y))})')
    else:
        if point_y > 0:
            print(f'(-{math.floor(abs(point_x))}, {math.floor(point_y)})')
        else:
            print(f'(-{math.floor(abs(point_x))}, -{math.floor(abs(point_y))})')


determine_closest(x_1, y_1, x_2, y_2)