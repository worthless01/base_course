def function(a, b, N):
    meaning = []
    step = (b-a) / (N-1)

    for i in range(N):
        x = a + i * step
        y = x * x
        meaning.append(y)
    
    return meaning

a = int(input('начало промежутка: '))
b = int(input('конец промежутка: '))
N = int(input('количество точек: '))

result = function(a, b, N)

print(f'значение функции y = x**2 от {a} до {b}:')

for i in range(N):
    x = a + i * (b - a) / (N - 1)
    print(f'x = {x}, y = {result[i]}')


import numpy as np

# y = f(x)

def f(a, b, N):
        x = np.linspace(a, b, N)
        y = x ** 2
        return y
    
y = f(-10, 10, 100)
print(y)