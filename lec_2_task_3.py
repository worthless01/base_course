b = int(input("Введите год: "))

if (b % 4 == 0 and b % 100 != 0) or (b % 400 == 0):
    print(f"Год {b} - високосный")
else:
    print(f"Год {b} - не високосный")