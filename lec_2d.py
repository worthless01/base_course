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

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Test')

plt.savefig('fig_8_1.png')