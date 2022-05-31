#!/usr/bin/python3
import sys


circle = sys.argv[1]  # 'circle'
dots = sys.argv[2]  # 'dots'

coord = []
with open(circle, 'r') as circle_file:
    for line in circle_file:
        coord.append(line.rstrip().split(' '))

x0 = int(coord[0][0])
y0 = int(coord[0][1])
r = int(coord[1][0])

coord_dots = []
with open(dots, 'r') as dots_file:
    for line in dots_file:
        coord_dots.append(line.rstrip().split(' '))


for i, coord in enumerate(coord_dots):
    x = float(coord[0])
    y = float(coord[1])

    if (x - x0)**2 + (y - y0)**2 < r**2:
        print(f'{i} - точка внутри')
        # print('(' + str(x) + '; ' + str(y) + ") - точна внутри")
    elif (x - x0)**2 + (y - y0)**2 == r**2:
        print(f'{i} - точка лежит на окружности')
        # print('(' + str(x) + '; ' + str(y) + ") - точка лежит на окружности")
    else:
        print(f'{i} - точка снаружи')
        # print('(' + str(x) + '; ' + str(y) + ") - точка снаружи")
