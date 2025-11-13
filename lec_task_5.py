import numpy as np
import math

N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))

trigonometry_array = np.zeros((N, M))

print(f"В массиве {M} столбцов (номера от 0 до {M-1})")
a = int(input("Введите номер первого столбца для обмена: "))
b = int(input("Введите номер второго столбца для обмена: "))

if a < 0 or a >= M or b < 0 or b >= M:
    print("Ошибка! Неправильные номера столбцов")
else:
    new_array = trigonometry_array.copy()
    
    for i in range(N):
        temp = new_array[i, a]
        new_array[i, a] = new_array[i, b]
        new_array[i, b] = temp
    
    print(f"\nМассив после замены столбцов {a} и {b}:")
    print(new_array)
    
    print("\nДля сравнения - исходный массив:")
    print(trigonometry_array)