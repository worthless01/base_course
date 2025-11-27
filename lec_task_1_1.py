def function(a, n):
    result = 1
    for i in range(n):
        result = result * a

    if n < 0:
        result = 1 / result 
    
    return result


int(input('введите целое число: '))
int(input('введите степень: '))