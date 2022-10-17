# --------------------------------------------
# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).
# --------------------------------------------
from functools import reduce
import random

# N = int(input("Введите число N: "))
# list = list(range(-N, N+1))
# pos = int(input("Введите размер списка позиций: "))
# positions = []
# for i in range(0, pos):
#     positions.append(random.randrange(0, pos+1))
# res = 1
# for i in positions:
#     res *= list[i]
# print(list)
# print(positions)
# print(f"Произведение элементов на указанных позициях: {res}")


# -----------------------------------------------------


N = int(input("Введите число N: "))
lst = [ _ for _ in range(-N, N+1)]
pos = int(input("Введите размер списка позиций: "))
positions = [random.randrange(0, pos+1) for _ in range(0, pos)]
res = reduce(lambda a, b: a * b,  positions)
print(lst)
print(positions)
print(f"Произведение элементов на указанных позициях: {res}")