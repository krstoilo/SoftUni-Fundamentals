import math

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())


def determine_closest(x1, y1, x2, y2):

    if abs(x1) > abs(x2) and abs(y1) > abs(y2):
        point_x = x2
        point_x2 = x1
        point_y = y2
        point_y2 = y1
    else:
        point_x = x1
        point_x2 = x2
        point_y = y1
        point_y2 = y2

    if point_x > 0:
        if point_y > 0:
            print(f'({math.floor(point_x)}, {math.floor(point_y)})({math.floor(point_x2)}, {math.floor(point_y2)})')
        else:
            print(f'({math.floor(point_x)}, -{math.floor(abs(point_y))})({math.floor(point_x2)}, {math.floor(point_y2)})')
    else:
        if point_y > 0:
            print(f'(-{math.floor(abs(point_x))}, {math.floor(point_y)})({math.floor(point_x2)}, {math.floor(point_y2)})')
        else:
            print(f'(-{math.floor(abs(point_x))}, -{math.floor(abs(point_y))})({math.floor(point_x2)}, {math.floor(point_y2)})')


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):

    if abs(x1) - abs(x2) > abs(x3) - abs(x4):
        point_x1 = x1
        point_y1 = y1
        point_x2 = x2
        point_y2 = y2
    else:
        point_x1 = x3
        point_y1 = y3
        point_x2 = x4
        point_y2 = y4

    determine_closest(point_x1, point_y1, point_x2, point_y2)


longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)