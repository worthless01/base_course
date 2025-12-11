flowers = ['роза', 'тюльпан', 'ромашка']
colors = [' красный', 'желтый', 'белый', 'фиолетовый', 'синий']

flowers_colors = dict(zip(flowers, colors))

print('cловарь: ')
for i, j in flowers_colors.items():
    print(f'{i}: {j}')