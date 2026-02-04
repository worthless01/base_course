import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 6.3, 0.01)

plt.plot(0.4*np.cos(t), 0.4*np.sin(t), color='r', lw=5)
plt.text(-0.17, -0.11, '+', color='black', fontsize=16)

plt.plot(2*np.cos(t), 2*np.sin(t), color='black', lw=1)
plt.plot(3*np.cos(t), 3*np.sin(t), color='black', lw=1)

np.random.seed(67)#одинаковая картинка была каждый раз
angles_random = np.random.uniform(0, 6.3, 7)#случайные электроны

for a in angles_random:
    plt.plot(2*np.cos(a), 2*np.sin(a), 'o', color='b')

np.random.seed(100)
angles_random = np.random.uniform(0, 6.3, 10)

for a in angles_random:
    plt.plot(3*np.cos(a), 3*np.sin(a), 'o', color='b')

plt.axis('equal')
plt.savefig('atom.png')