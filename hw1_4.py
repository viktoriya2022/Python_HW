# ------------------------------------------------------------------------
# Напишите программу, которая по заданному номеру четверти показывает диапазон 
# возможных координат точек в этой четверти (X и Y).
# ------------------------------------------------------------------------

quarter_num = int(input("Введите номер четверти координатной плоскости: "))

if quarter_num == 1:
    print(f'В I четверти координатной плоскости X ∈(0; + ∞), Y ∈(0; + ∞)')
elif quarter_num == 2:
    print(f'Во II четверти координатной плоскости X ∈(- ∞; 0), Y ∈(0; + ∞)')
elif quarter_num == 3:
    print(f'В III четверти координатной плоскости X ∈(- ∞; 0), Y ∈(- ∞; 0)')
elif quarter_num == 4:
    print(f'В IV четверти координатной плоскости X ∈(0; + ∞), Y ∈(- ∞; 0)')
else:
    print("Что-то пошло не так. Попробуйте ввести число от 1 до 4.")