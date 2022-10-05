#  -------------------------------------------------------
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  -------------------------------------------------------

import random

n = int(input('Введите количество чисел в списке: '))
numbers = []
for i in range(n):
    numbers.append(random.randint(0, 10))
print(f'Исходный список: {numbers}')

list = []
i = 0
while i < (n-1) / 2:
    num = numbers[i] * numbers[n-1-i]
    list.append(num)
    i += 1 
print(f'Список произведений: {list}')    
