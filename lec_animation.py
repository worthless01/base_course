import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


# Создание пространства и подпространства для анимации
fig, ax = plt.subplots()

# Объект анимации
anim_object, = plt.plot([], [], '-', lw=2)  #запятая после object создает картеж

x, y = [], [] # Координаты объекта анимации
frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(5, 5*np.pi) # Пределы изменения переменной Х
ax.set_ylim(-5, 5) # Пределы изменения переменной У

# Функция подстановки параметра в объект анимации
def update(frame):
    x.append(5*(4-np.sin(4))) # Расчет координаты Х
    y.append(5*(1-np.cos(4))) #Расчет координаты Y

    # Передача координат объекту анимации
    anim_object.set_data(x, y)

    return anim_object


ani = FuncAnimation(fig, # Вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=frames_interval, # Интервал значений
                    interval=50)# Интервал между кадрами,
                                # по умолчанию 200 милисекунд

ani.save('dz_2.gif', writer="pillow")

