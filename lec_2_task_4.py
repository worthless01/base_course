#a = int(input('кол-во чисел: '))

#b, c = 0, 1
#print('ряд: ')
#for i in range(a):
   # print(a, end=' ')
    #b, c=c, b+c

a = int(input('кол-во чисел: '))
b=0
c=1
for i in range(a):
    print(b, end=' ')
    k=b+c
    b=c
    c=k