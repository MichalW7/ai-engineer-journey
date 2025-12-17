import numpy as np
#Zad 1
a=np.array([1, 2, 3, 4, 5])
print(a*2)
print(a+10)
print(a**2)
#
#Zad 2
a = np.array([-3, -1, 0, 2, 4, 5])
mask=a>2
print(a[mask])
#
#Zad 3
a = np.array([-5, -2, 0, 1, 3, 6])
print(a[a>0]**2)
#