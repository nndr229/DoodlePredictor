from tkinter import *
from PIL import Image,ImageDraw
import numpy as np
# import Image, ImageDraw

class Doodle_submitter:
	def __init__(self):
		self.root = Tk()

		self.canvas = Canvas(self.root, bg='white', width=400, height=400)
		self.canvas.grid(row=1, columnspan=5)

		self.submit_button = Button(self.root, text='submit', command=self.use_submit)
		self.submit_button.grid(row=0, column=0)
		
		self.image1 = Image.new("RGB", (400, 400), (0,0,0))
		self.draw = ImageDraw.Draw(self.image1)

		self.clear_button = Button(self.root, text='clear', command=self.clear)  #, command=self.use_pen)
		self.clear_button.grid(row=0, column=1)

		self.canvas.bind('<B1-Motion>', self.paint)
		self.canvas.bind('<ButtonRelease-1>')
		print("JJJJJJJJJ")
		self.points_array = []
		self.filename =None

		self.root.mainloop()

		
	def use_submit(self):
		# print(points_array)
		self.draw.line((self.points_array),(255,255,255),width=13)

		self.filename = "my_drawing.bmp"
		self.image1.save(self.filename)

	def paint(self,event):
		self.canvas.create_line(event.x,event.y,event.x,event.y, fill="red",width="10",capstyle=ROUND, smooth=TRUE)
		
		self.points_array.append((event.x,event.y))

   
	def clear(self):
		self.canvas.delete('all')
		self.points_array=[]
		os.remove(self.filename)
		self.image1 = Image.new("RGB", (400, 400), (0,0,0))
		self.draw = ImageDraw.Draw(self.image1)




if __name__ == '__main__':
	Doodle_submitter()    








# from tkinter import *

# class Doodle_submitter:
#     def __init__(self):
#         self.root = Tk()

#         self.canvas = Canvas(self.root, bg='white', width=300, height=300)
#         self.canvas.grid(row=1, columnspan=5)

#         self.submit_button = Button(self.root, text='submit', command=self.use_submit)
#         self.submit_button.grid(row=0, column=0)
		

#         self.clear_button = Button(self.root, text='clear', command=self.clear)  #, command=self.use_pen)
#         self.clear_button.grid(row=0, column=1)

#         self.canvas.bind('<B1-Motion>', self.paint)
#         self.canvas.bind('<ButtonRelease-1>')
#         self.points_array = []

#         self.root.mainloop()

		
#     def use_submit(self):
#         print(self.points_array)
#         return self.points_array

#     def paint(self,event):
#         self.canvas.create_line(event.x,event.y,event.x+1,event.y, fill="red",width="5",capstyle=ROUND, smooth=TRUE)
#         self.points_array.append((event.x,event.y))

   
#     def clear(self):
#         self.canvas.delete('all')
#         self.points_array=[] 




# if __name__ == '__main__':
#     Doodle_submitter()    