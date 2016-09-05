# By Marlon H (cc) with <3

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Leitura da imagem

im1 = Image.open('marilyn.jpg')
(l,h) = im1.size
out = Image.new(im1.mode, (l,h))

# Histograma

histograma = im1.histogram()

plt.plot(histograma)
plt.ylabel('Histograma')
plt.show()
