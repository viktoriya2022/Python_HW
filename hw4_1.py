# ------------------------------------------------------
# 1 Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1) <= d <= 10^(-10)
# ------------------------------------------------------
import math

number = input('Задайте точность: ')
d = str(number)
new_d = (abs(d.find('.') - len(d)) - 1)


num = math.pi
print(round(num,new_d)) 