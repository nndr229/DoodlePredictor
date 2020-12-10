from PIL import Image
import PIL
import numpy as np
from skimage.transform import resize

im = Image.open("my_drawing.bmp")
newsize = (28, 28) 
im = im.resize(newsize, Image.ANTIALIAS) 

im.show()

im2= im.convert("1")
ary = np.array(im2)
im2.show()

output_array=[]
zero=ary[0][0]

for j in range(len(ary)):
	for i in range(28):
		output_array.append(ary[j][i])	

for i in range(len(output_array)):
	if output_array[i]==zero:
		output_array[i]=0
	else:
		output_array[i]=1	

img = Image.new('1', (28, 28))
pixels = img.load()

data=output_array
print("------------------------------")
print("------------------------------")
print("------------------------------")

data[:] = [data[i:i + 28] for i in range(0, 784,28)]

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = data[i][j],
        
img = img.rotate(270, PIL.Image.NEAREST, expand = 1) 
img.show()
