# ----------------------------------------------------------
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# ----------------------------------------------------------

import math
x_coord_first = int(input("Введите координату Х точки А: "))
y_coord_first = int(input("Введите координату Y точки А: "))
x_coord_second = int(input("Введите координату Х точки B: "))
y_coord_second = int(input("Введите координату Y точки B: "))

lenAB = round(math.hypot(x_coord_first-x_coord_second, y_coord_first-y_coord_second),2)
print(f'Расстояние между точками А и В: {lenAB} ')

