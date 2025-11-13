import numpy as np
import math

# Задача №4
N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))

trigonometry_array = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        value = math.sin(2*N - j)
        
        if value < 0:
            trigonometry_array[i, j] = 0
        else:
            trigonometry_array[i, j] = value

print("\nДвумерный массив trigonometry_array:")
print(trigonometry_array)

# Задача №5

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