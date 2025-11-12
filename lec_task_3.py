import numpy as np
from physical_constants import g

x0=0
y0=0
v0=20
a=45

t=np.array([0, 1, 2, 3, 4, 5])

vx=v0*np.cos(np.radians(a))
vy=v0*np.sin(np.radians(a))

x=x0+vx*t 
y=y0+vy*t-(g*t**2)/2
 
ravno=np.column_stack((t, x, y))
print(ravno)