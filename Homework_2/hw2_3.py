# ---------------------------------------
# Задать список из n чисел последовательности (1+ 1/n)^n и вывести на экран их сумму.
# ---------------------------------------

num = int(input("Введите число N: "))
res = []
sum = 0
for i in range(1, num + 1):
    result = (1 + 1/i)**i
    res.append(result)
    sum = sum + round(result,2)
print(*res, sep=', ')
print(f'Сумма: {sum}')