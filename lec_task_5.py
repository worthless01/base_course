import numpy as np
import math

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

print("Двумерный массив trigonometry_array:")
print(trigonometry_array)

a = int(input('1 столбец для замены: '))
b = int(input('2 столбец для замены: '))

trigonometry_array[:, [a, b]] = trigonometry_array[:, [b, a]]
print()
print(trigonometry_array)
