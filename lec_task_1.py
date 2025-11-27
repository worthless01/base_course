# def a():
    
#     n = int(input('кол-во чисел: '))
#     numbers = []
#     for i in range(n):
#         num = int(input(f'Введите число {i+1}: '))
#         numbers.append(num)
        
#     arithmetic = sum(numbers) / n
#     return arithmetic

# result = a()
# print(f'ср арифметическое равно:{result}')

import numpy as np

def mean_func(array):
    return np.mean(array)

test = np.array([3, 5, 6, 7, 8])
result = mean_func(test)
print(f'среднее арифм равно: {result}')









def mean_arifmetic(array):
    s = 0
    for element in array:
        s = s + element

    print(s / len(array))
    return s / len(array)

test = np.array([3, 6, 7, 9, 1])
mean_arifmetic(test)







def mean_arifmetic(*arg):
    s = 0
    if len(arg) > 1:
        for element in arg:
            s = s + element
            len_arg = len(arg)
    else:
        for element in arg[0]:
            s = s + element
            len_arg = len(arg[0])
        
    print(s / len(arg[0]))
    return s / len(arg[0])

test = np.array([3, 6, 7, 9, 1])
mean_arifmetic(test)