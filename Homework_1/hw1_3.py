# ------------------------------------------------------------------------
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# ------------------------------------------------------------------------

x = int(input("Введите кординату X: "))
y = int(input("Введите кординату Y: "))

if x == 0 and y == 0:
    print(f'Точка с координатами [{x}; {y}] находится в центре координатной оси.')
elif x == 0:
    print(f'Точка с координатами [{x}; {y}] находится на координатной оси Y.')
elif y == 0:
    print(f'Точка с координатами [{x}; {y}] находится на координатной оси X.')
elif x > 0 and y > 0:
    print(f'Точка с координатами [{x}; {y}] находится в 1 четверти координатной плоскости.')
elif x < 0 and y < 0:
    print(f'Точка с координатами [{x}; {y}] находится в 3 четверти координатной плоскости.')
elif x > 0 and y < 0:
    print(f'Точка с координатами [{x}; {y}] находится в 4 четверти координатной плоскости.')
elif x < 0 and y > 0:
    print(f'Точка с координатами [{x}; {y}] находится вo 2 четверти координатной плоскости.')
else:
    print("Что-то пошло не так")