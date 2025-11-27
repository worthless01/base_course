import constant_module as cm

def square():
    print('выберите фигуру: ')
    print('круг - 1')
    print('треугольник - 2')
    print('прямоугольник - 3')

    choice = int(input('введите номер 1-3:'))
    
    if choice == 1:
        r = int(input('радиус круга: '))
        S_circle = cm.pi * r ** 2
        print(f'площадь круга: {S_circle}')

    elif choice == 2:
        a = int(input('сторона треугольника: '))
        h = int(input('высота треугольника: '))
        S_triangle = (a * h) / 2
        print(f'площадь треугольника: {S_triangle} ')

    elif choice == 3:
        c = int(input('1 сторона прямоугольника: '))
        k = int(input('2 сторона прямоугольника: '))
        S_rectangle = c * k 
        print(f'площадь прямоугольника: {S_rectangle} ')
    
    else:
        print('выбор не подходит')

square()