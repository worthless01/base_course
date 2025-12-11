import matplotlib.pyplot as plt
import numpy as np

def hyperbola(k=7, x=0):
   
    x = np.arange(-10, 10, 1)
    y = k / x

    plt.plot(x, y, label = 'my hyperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('hyperbola')
    plt.axis('equal')
    plt.legend()

    plt.savefig('DZ_2.png')

if __name__ == '__main__':
    hyperbola()