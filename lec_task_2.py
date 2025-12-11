name = 'name surname'

up = '_'.join(name.upper()) + '_'
up_codes = [ord(simbol) for simbol in up]
print(up)

low = '_'.join(name.lower()) + '_'
low_codes = [ord(simbol) for simbol in low]
print(low)

print('up:', up_codes)
print('low:', low_codes)

all = up_codes + low_codes

print('max:', max(all))
print('min:', min(all))