name = 'name surname patronymic'

up = (name.upper()) 
print(up)

up_codes = [ord(simbol) for simbol in up]
print(up_codes)

sum_up = sum(up_codes)
print(sum_up)


print()


low = (name.lower()) 
print(low)

low_codes = [ord(simbol) for simbol in up]
print(low_codes)

sum_low = sum(low_codes)
print(sum_low)


print()


print(sum_up + sum_low)