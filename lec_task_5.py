
name = 'name surname patronymic'

summ_up = sum(ord(name.upper()) for name in name)
summ_low = sum(ord(name.lower()) for name in name)
print(f'сумма капс: {summ_up}')
print(f'сумма обычный: {summ_low}')
print(f'вся сумма: {summ_up + summ_low}')