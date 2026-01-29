import matplotlib.pyplot as plt
import numpy as np


def Astroid (R=3/4):
    alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)  # Параметр

    x = R * (np.cos(alpha) ** 3 )
    y = R * (np.sin(alpha) ** 3 )

    plt.plot(x, y, ls='-', lw=3)
    plt.axis('equal')
    plt.savefig('Astroid.png')


if __name__ == '__main__':
    Astroid()