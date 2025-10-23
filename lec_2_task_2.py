a = int(input('введите первый член: '))
b = int(input('введите знаменатель:'))
c = int(input('введите количество членов:'))

print('геом прогрессия: ')

for i in range(c):
    q = a*(b**c)
    print(q)