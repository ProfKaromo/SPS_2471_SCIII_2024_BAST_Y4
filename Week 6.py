#Python Operators
#Arithmetic
#+,-,*,/
#import numpy as np
k1 = [3,5,6,7]
k2 = [9,3,5,2]
results = [x+y for x,y in zip(k1,k2)]
print(results)

w = 9
y = 3

z = w+y
print(z)
#v1 = np.array([3,5,6,7])
#v2 = np.array([9,3,5,2])
#a1 = v1+v2

#Comparison Operators
#>,<,>=,<=,==,!=

print(w<y)
print(w>y)
k1 = [14,5,6,7]
k2 = [9,3,5,2]
print(k1<k2)
#Logical Operators
#&,|,&&,||,!

print((w!=y))

#Miscelineous
#%*%,%in%,: