import physical_constants as pc
import lec_number as nb
import math 

a=nb.h*pc.g*(math.tan(nb.b)**2)

b=2*(math.cos(nb.a)**2)*(1-math.tan(nb.a)*math.tan(nb.b))

v=math.sqrt(a/b)

print(v)

N=(2/math.sqrt(nb.p))*math.sqrt(pc.h)*(((pc.k)*(nb.T))**(3/2))*((pc.e)**(nb.e/(pc.k*nb.T)))*((nb.e)**(nb.T/2))

print(N)