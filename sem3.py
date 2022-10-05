# def my_func():  # ничего не принимает
#     x = 3
#     y = 5
#     return x, y

# # вызываем функцию
# z = my_func()
# print(z)
# print(type(z))    # выводит на печать тип данных
# a, b = z          # распаковали кортеж
# print(a, b)


# --------------------------------
# 2 Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.
# --------------------------------

# # задание списка строк
# def input_string():
#     list_string = input('Введите элементы списка через пробел:')
#     list_string = list_string.split(' ')  #  Разделение элементов списка запятой с пробелом
#     return list_string


# def find_number_in_list(list_string, number):
#     for item in list_string:
#         if str(number) in item:            # поиск подстроки в строке
#             print(f'В элементе списка {list_string} есть число {number}')

# list_string = input_string()
# print(f'Список строк: {list_string}')
# number = int(input('Введите число для поиска'))
# find_number_in_list(list_string, number)

# --------------------------------
# Напишите программу, которая определит позицию второго вхождения строки в списке либо
# сообщит, что её нет.
# --------------------------------
