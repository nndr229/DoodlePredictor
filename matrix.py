import random
import math
import numpy as np


class Matrix:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.data = []

		for i in range(self.rows):
			self.data.append([])
			inner_row = self.data[i]
			for j in range(self.cols):
				inner_row.append(0)

	# def __repr__(self):
	# 	return f"The matrix has {self.rows} rows  and {self.cols} columns"
	# 	if self.rows > 0 and self.cols > 0:
	# 		for i in range(len(self.data)):
	# 			print(self.data[i])
	# 		print()

	def get_matrix(self):
		if self.rows > 0 and self.cols > 0:
			for i in range(len(self.data)):
				print(self.data[i])
			print()
			return self.data

	def scalar_multiply(self, n):
		if isinstance(n, Matrix):
			for i in range(len(self.data)):
				for j in range(len(self.data[i])):
					self.data[i][j] *= n.data[i][j]
		else:
			for i in range(len(self.data)):
				for j in range(len(self.data[i])):
					self.data[i][j] *= n
		return self.data

	def mapper(self,func):
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				val = self.data[i][j]
				self.data[i][j] = func(val)
		return self.data


	@staticmethod
	def map(matrix,func):
		result = Matrix(matrix.rows, matrix.cols)
		for i in range(len(matrix.data)):
			for j in range(len(matrix.data[i])):
				val = matrix.data[i][j]
				result.data[i][j] = func(val)

		return result
						 
	@staticmethod
	def fromArray(arr):
		m = Matrix(len(arr),1)
		for i in range(len(arr)):
			m.data[i][0]=arr[i]

		return m	
	@staticmethod
	def subtract(a,b):
		result = Matrix(a.rows,a.cols)
		for i in range(len(result.data)):
			for j in range(len(result.data[i])):
				result.data[i][j] = a.data[i][j] - b.data[i][j] 
		return result



	def add(self, n):
		if isinstance(n, Matrix):
			for i in range(len(self.data)):
				for j in range(len(self.data[i])):
					self.data[i][j] += n.data[i][j]
		else:
			for i in range(len(self.data)):
				for j in range(len(self.data[i])):
					self.data[i][j] += n
		return self.data

	def toArray(self):
		arr =[]
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				arr.append(self.data[i][j])
		return arr		
		

	def randomize(self):
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				self.data[i][j] = random.uniform(-1,1)
				# self.data[i][j] = math.floor(self.data[i][j])

	@staticmethod
	def multiply(m,n):
		if type(n) == Matrix:
			if(m.cols != n.rows):
				print("Columns of A must match the rows of B")
			else:
				result = Matrix(m.rows,n.cols)
				for i in range(result.rows):
					for j in range(result.cols):
						sum = 0
						for k in range(m.cols):
							sum += m.data[i][k] * n.data[k][j]
						result.data[i][j] =sum
			return result			
	@staticmethod
	def transpose(a):
		new = Matrix(a.cols, a.rows)

		for i in range(len(new.data)):
			for j in range(len(new.data[i])):
				new.data[i][j] = a.data[j][i]
		return new


def double(*args):
	for arg in args:
		return 2*arg



# arr=[0.07784910804854898
# , 0.12714684771058138
# , 0.14475653622995846]
# m=Matrix.fromArray(arr)
# arr2=[0.914910703587472]
# n=Matrix.fromArray(arr2)

# m.scalar_multiply(n)
# m = Matrix(2, 3)
# # print(m)
# m.get_matrix()

# m.randomize()
# m.get_matrix()
# print("transpose")
# a = Matrix.transpose(m)
# a.get_matrix()
# # # print(np.transpose(m.data))



# # m.map(double)
# # m.get_matrix()


# n = Matrix(2, 3)
# n.randomize()
# n.get_matrix()

# result = Matrix.subtract(m,n)
# result.get_matrix()



# result =Matrix.multiply(m,n)
# result.get_matrix()

# a = np.array([m.data])
# b = np.array([n.data])

# print(a.dot(b))

# [38, 62]
# [107, 47]


# [0.07784910804854898]
# [0.12714684771058138]
# [0.14475653622995846]

# [[0.914910703587472]]