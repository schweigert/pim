from ia636 import *

f = iaread('lena.pgm')
iashow(f)

histograma = range(0,255)

for i in range(0,255):
    histograma[i] = 0

print(type(f))
for i in f:
    for j in i:
        histograma[j] += 1

import matplotlib.pyplot as plt
plt.plot(histograma)
plt.ylabel('Histograma')
plt.show()
