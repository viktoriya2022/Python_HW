# ------------------------------------------------------
# 4 Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# ------------------------------------------------------

from random import randint
 
k = int(input('Задайте степень k: '))
 
def create_new_file(f):
    with open('hw4_4.txt', 'w') as data:
        data.write(f)
 
def create_new_list(k):
    list_num = []
    for i in range(k + 1):
        list_num.append(randint(0, 101))    
    return list_num
    
def create_polynom(p):
    list = p[::-1]
    pol = ''
    if len(list) < 1:
        pol = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                pol += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    pol += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                pol += f'{list[i]}x'
                if list[i + 1] != 0:
                    pol += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                pol += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                pol += ' = 0'
    return pol
 
res = create_new_list(k)
create_new_file(create_polynom(res))
print(f'Многочлен вида: {create_polynom(res)} записан в файл "hw4_4.txt"')