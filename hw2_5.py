# ------------------------------------
# Реализовать алгоритм перемешивания списка.
# ------------------------------------

import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def mix_list(list):
    # Создаем копию списка
    list = list[:]
    for i in range(len(list)):
        # Получение случайного индекса
        index = random.randint(0, len(list) - 1)
        # Замена
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    # Возвращаем список
    return list
mixed_list = mix_list(list)
print("Исходный список: ")
print(*list, sep=', ')
print("Итоговый список: ")
print(*mixed_list, sep=', ')

