from PIL import Image
from numpy import *
from scipy.ndimage import filters


img = Image.open('lena_B.png')
(l,h) = img.size
'''
# Sobel derivative filters
imx = zeros(im.shape)
filters.sobel(im,1,imx)

imy = zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = sqrt(imx**2+imy**2)

print(type(imx))
im = Image.fromarray(imy + imx)

'''
out = Image.new('L', (l,h))
def linearf(x, i, j):
    x = x  * x / (x + 2)
    return int(x), j, i


for i in range(0,l):
   for j in range(0,h):
       pix, px, py = linearf(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('TransLinear.png')
