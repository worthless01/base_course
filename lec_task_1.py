import matplotlib.pyplot as plt

x = [1, 1, 5, 5, 1]
y = [1, 5, 5, 1, 1]
plt.plot(x, y, color='m', marker='o', ms=7)
plt.axis('equal')
plt.grid() 
plt.title('DZ_1')


plt.savefig('dz.png')