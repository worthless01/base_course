def a():
    
    n = int(input('кол-во чисел: '))
    numbers = []
    for i in range(n):
        num = int(input(f'Введите число {i+1}: '))
        numbers.append(num)
        
    arithmetic = sum(numbers) / n
    return arithmetic

result = a()
print(f'ср арифметическое равно:{result}')
    