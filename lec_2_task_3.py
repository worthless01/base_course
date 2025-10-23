b = int(input("Введите год: "))

if b % 4 == 0 and b !=0:
    print(f"Год {b} - високосный")
else:
    print(f"Год {b} - не високосный")