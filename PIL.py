from PIL import Image
import numpy as np
imagem1=Image.open('balao.jpg')
(l,h)=imagem1.size
print(l,h)
out=Image.new(imagem1.mode, (l,h))
for j in range(0, h):
    for i in range(0, l):
        out.putpixel((i,j),imagem1.getpixel((i,j)))
        print(imagem1.getpixel((i,j)))
out.show()
out.save("outLenaShort.jpg","JPEG")
