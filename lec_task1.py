import matplotlib.pyplot as plt
import numpy as np


def Cycloid(R=3):
    alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)  # Параметр

    x = R * (alpha - np.sin(alpha))
    y = R * (1 - np.cos(alpha))

    plt.plot(x, y, ls='-', lw=3)
    plt.axis('equal')
    plt.savefig('Cycloid.png')


if __name__ == '__main__':
    Cycloid()