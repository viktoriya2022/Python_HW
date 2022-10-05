# ------------------------------------------
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# ------------------------------------------

import random

n = int(input('Введите количество чисел в списке: '))
numbers = []
for i in range(n):
    numbers.append(random.randint(0, 10))
print(numbers)

odd_numbers_sum = 0
i = 1
while i < n:
    odd_numbers_sum += numbers[i]
    i+=2
print(f'Сумма чисел на нечетных позициях: {odd_numbers_sum}')    
