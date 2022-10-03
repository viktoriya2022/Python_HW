# --------------------------------------------
# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).
# --------------------------------------------
import random

N = int(input("Введите число N: "))
list = list(range(-N, N+1))
print(list)

pos = int(input("Введите размер списка позиций: "))
positions = []
for i in range(0, pos):
    positions.append(random.randrange(0, pos+1))
print(positions)

res = 1
for i in range(0, pos):
        res *= list[positions[i]]
print(f"Произведение элементов на указанных позициях: {res}")