# -----------------------------------
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# -----------------------------------


# РЕШЕНИЕ НЕ ВЕРНО. СРАВНИВАЮТСЯ САМИ ЧИСЛА, А НЕ ИХ ДРОБНЫЕ ЧАСТИ.


from random import uniform


n = int(input('Введите количество элементов списка: '))
numbers = []
for i in range(n):
    numbers.append(round((uniform(0, 9)), 2))
num_min = numbers[0]
num_max = numbers[0]
for i in range(len(numbers)):    
    if num_max < numbers[i]:
        num_max = numbers[i]
    if num_min > numbers[i]:
        num_min = numbers[i]
dif = abs((num_max - int(num_max)) - (num_min - int(num_min)))

print(numbers)
print(f'Максимальное значение: {num_max}')
print(f'Минимальное значение: {num_min}')
print(f'Разница: {(round(dif, 2))}')
