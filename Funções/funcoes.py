from ia636 import *
import math

f = iaread('lena.pgm')
iashow(f)
for i in range(0,len(f)):
    for j in range(0,len(f[i])):
        f[i][j] = math.log(f[i][j])

iashow(f)
