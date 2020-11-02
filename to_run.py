from neural_network import NeuralNetwork
from matrix import Matrix
import  numpy as np
import random
from tkinter import *
from PIL import Image,ImageDraw
from skimage.transform import resize
from tkinter.messagebox import showinfo
import os
import PIL
output=[]

data_cats = np.load("data/cats_10000.npy")
data_trains = np.load("data/laptops_10000.npy")
data_brooms = np.load("data/brooms_10000.npy")

data_cats =list(data_cats)
data_trains =list(data_trains)
data_brooms=list(data_brooms)


cats_training=[]
cats_testing = []

nn = NeuralNetwork(784,64,3)

for i in range(len(data_cats)):
	if i <8000:
		cats_training.append(data_cats[i])
	else:
		cats_testing.append(data_cats[i])

trains_training = []
trains_testing=[]

for i in range(len(data_trains)):
	if i <8000:
		trains_training.append(data_trains[i])
	else:
		trains_testing.append(data_trains[i])

brooms_training=[]
brooms_testing =[]

for i in range(len(data_brooms)):
	if i <8000:
		brooms_training.append(data_brooms[i])
	else:
		brooms_testing.append(data_brooms[i])




def run_nn():
	global nn
	for i in range(1):
		input_choice = random.choice([0,1,2])
		index = random.randint(0,7999)
		taget=0
		input_list=[]
		if input_choice==0:
			input_list=cats_training
			target=[1,0,0]
		elif input_choice==1:
			input_list=trains_training
			target=[0,1,0]
		elif input_choice==2:
			input_list=brooms_training
			target=[0,0,1]
		nn.train(input_list[index],target)

	d=Doodle_submitter()





#Output for 10000 iterations for input cat,train,broom lr=0.1
# [0.7670178117987388, 0.34350717864559543, 0.007863469788537946]
# [0.15432569789952252, 0.9016315841213937, 0.005107874882420323]
# [0.03878504854789654, 0.02076229806294787, 0.9674263203704581]



class Doodle_submitter:
	def __init__(self):
		self.root = Tk()
		self.percentage =0
		self.canvas = Canvas(self.root, bg='white', width=400, height=400)
		self.canvas.grid(row=1, columnspan=5)

		self.submit_button = Button(self.root, text='submit', command=self.use_submit)
		self.submit_button.grid(row=0, column=0)

		self.train_button = Button(self.root, text='train nn', command=self.use_train)
		self.train_button.grid(row=0, column=2)

		self.test_button = Button(self.root, text='test nn', command=self.use_test)
		self.test_button.grid(row=0, column=3)

		self.image1 = Image.new("RGB", (400, 400), (0,0,0))
		self.draw = ImageDraw.Draw(self.image1)


		self.clear_button = Button(self.root, text='clear', command=self.clear)  #, command=self.use_pen)
		self.clear_button.grid(row=0, column=1)

		self.canvas.bind('<B1-Motion>', self.paint)
		self.canvas.bind('<ButtonRelease-1>')

		self.points_array = []
		self.filename =None

		self.root.mainloop()


	def use_submit(self):
		# print(points_array)
		global nn


		self.draw.line((self.points_array),(255,255,255),width=13)

		self.filename = "my_drawing.bmp"
		# self.image1=self.image1.rotate(90, PIL.Image.NEAREST, expand = 1)
		self.image1.save(self.filename)
		im = Image.open("my_drawing.bmp")
		newsize = (28, 28)
		im = im.resize(newsize)

		im2= im.convert("1")
		ary = np.array(im2)
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



		output=nn.feed_forward(output_array)
		output_text=""
		if output[0] >0.7:
			output_text="CAT"
		elif output[1] >0.7:
			output_text="LAPTOP"
		elif output[2] >0.7:
			output_text="BROOM"
		else:
			output_text="CAN'T DECIDE!"
		self.canvas.create_text(200,10,fill="darkblue",font="Times 14 italic bold",text=output_text)
		self.canvas.create_text(200,25,fill="darkblue",font="Times 8 italic bold",text=str(output))
		self.canvas.update

	def use_train(self):
		global cats_training,trains_training,brooms_training
		for i in range(100):
			input_choice = random.choice([0,1,2])
			index = random.randint(0,7999)
			taget=0
			input_list=[]
			if input_choice==0:
				input_list=cats_training
				target=[1,0,0]
			elif input_choice==1:
				input_list=trains_training
				target=[0,1,0]
			elif input_choice==2:
				input_list=brooms_training
				target=[0,0,1]
			nn.train(input_list[index],target)

	def use_test(self):
		global cats,testing,brooms_testing,trains_testing
		number_of_correct=0
		for i in range(100):
			input_choice = random.choice([0,1,2])
			index = random.randint(0,2000)
			taget=0
			input_list=[]
			if input_choice==0:
				input_list=cats_testing
				target=[1,0,0]
			elif input_choice==1:
				input_list=trains_testing
				target=[0,1,0]
			elif input_choice==2:
				input_list=brooms_testing
				target=[0,0,1]

			output=nn.feed_forward(input_list[index])

			if input_choice==0:
				if output[0]>0.8:
					number_of_correct+=1
			elif input_choice==1:
				if output[1]>0.8:
					number_of_correct+=1
			elif input_choice==2:
				if output[2]>0.8:
					number_of_correct+=1
		self.percentage = (number_of_correct/100)*100
		self.popup_showinfo()

	def popup_showinfo(self):
		showinfo("Testing Output",f"Testing complete! Accuracy is {self.percentage}")



	def paint(self,event):
		self.canvas.create_line(event.x,event.y,event.x,event.y, fill="red",width="20",capstyle=ROUND, smooth=TRUE)

		self.points_array.append((event.x,event.y))


	def clear(self):
		self.canvas.delete('all')
		self.points_array=[]
		os.remove(self.filename)
		self.image1 = Image.new("RGB", (400, 400), (0,0,0))
		self.draw = ImageDraw.Draw(self.image1)

run_nn()
