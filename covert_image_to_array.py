from PIL import Image
import PIL
import numpy as np
from skimage.transform import resize


im = Image.open("my_drawing.bmp")
newsize = (28, 28) 
im = im.resize(newsize, Image.ANTIALIAS) 

im.show()


# img = Image.open('my_drawing.bmp')

im2= im.convert("1")
ary = np.array(im2)
# print(ary)
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



print(output_array)
# # Split the three channels
# r,g,b = np.split(ary,3,axis=2)
# r=r.reshape(-1)
# g=r.reshape(-1)
# b=r.reshape(-1)

# # Standard RGB to grayscale 
# bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
# zip(r,g,b)))
# bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
# bitmap = np.dot((bitmap > 128).astype(float),255)
# print(list(bitmap))
img = Image.new('1', (28, 28))
pixels = img.load()

data=output_array
# print(data1[467])
print("------------------------------")
print("------------------------------")
print("------------------------------")

data[:] = [data[i:i + 28] for i in range(0, 784,28)]

# zero = data[0][0]
# data=list(data)

# count=0
# for i in range(len(data)):
# 	for j in range(28):
# 		count+=1
# 		if data[i][j] == zero:
# 			data[i][j]=False
# 		else:
# 			data[i][j]=True	







for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = data[i][j],
# print(pixels)        
        
img = img.rotate(270, PIL.Image.NEAREST, expand = 1) 
img.show()