# ------------------------------------------------------
# 2 Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.
# ------------------------------------------------------

num = int(input('Задайте число: '))
n = num
i = 2
simple_numbers = []
while i * i <= n:
    while n % i == 0:
        simple_numbers.append(i)
        n = n // i
    i = i + 1
if n > 1:
    simple_numbers.append(n)
print(f'Простые множители числa {num}: ',end='')
print(*simple_numbers, sep=', ')
