import numpy as np
import matplotlib.pyplot as plt

# Создание 3D-пространства
fig, ax = plt.subplots(subplot_kw={'projection':'3d'})

# Определение параметров кривой
t = np.arange(0.01, 4*np.pi, 0.01)
R = 1

# Параметрическое задание пространственной кривой
x = R * np.cos(t)
y = R * np.sin(t)
z = R * np.log10(t)

# Построение пространственной кривой
ax.plot(x, y, z, label='Dich')

ax.set_xlable('X')
ax.set_ylable('Y')
ax.set_zlable('Z')

ax.set_title('3D Test')

plt.savefig('fig_1.png')
