from PIL import Image
import numpy

#########
##
##

nrCores = 6

##
##
########

img = Image.open('lena_B.png')
(l,h) = img.size
delta = 256/nrCores
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
def linear(x, i, j):
    coisa = delta
    if x < coisa:
        return 0, i, j
    while x > coisa:
        coisa = coisa + delta
    return coisa, i, j

for i in range(0,l):
   for j in range(0,h):
       pix, px, py = linear(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('DiminuirBits.png')

####################################################################################
####################################################################################
####################################################################################
