from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def Cycloid(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 5*np.pi, 0.01)
    x = R*(alpha - np.sin(alpha))
    y = R*(alpha - np.cos(alpha))
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='g', label='line')


def animate(i):
    ball.set_data(Cycloid(R=0, vx0=0.01, vy0=0.01, time=i))
    return ball


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('dz_1.gif', writer="pillow")

