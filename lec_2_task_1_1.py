a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

#k=a*x**2+b*x+c

D=b**2-4*a*c

if D>0:

x1=(-b+1/2*D):(2*a)
x2=(-b-1/2*D):(2*a)
print(f'два корня: x1={x1}, x2={x2}')

elif D==0:

