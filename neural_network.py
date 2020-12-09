from matrix import Matrix
import  math
class NeuralNetwork:
	def __init__(self,input_nodes,hidden_nodes,output_nodes):
		self.input_nodes = input_nodes
		self.hidden_nodes = hidden_nodes
		self.output_nodes = output_nodes

		self.weights_ih = Matrix(self.hidden_nodes,self.input_nodes)
		self.weights_ho = Matrix(self.output_nodes,self.hidden_nodes)
		self.weights_ih.randomize()
		self.weights_ho.randomize()

		self.bias_h = Matrix(self.hidden_nodes,1)
		self.bias_o = Matrix(self.output_nodes,1)
		self.bias_h.randomize()
		self.bias_o.randomize()

		self.learning_rate = 0.1

	# @staticmethod
	# def sigmoid(*args):
	# 	for x in args:
	# 		return 1/(1+Math.exp(-x))

	def feed_forward(self,input_array):
		#Generating the hidden outputs
		inputs = Matrix.fromArray(input_array)
		hidden = Matrix.multiply(self.weights_ih,inputs)
		hidden.add(self.bias_h)
		#activation function
		# print("--------------------")
		# print("----------------")
		hidden.mapper(sigmoid)

		output = Matrix.multiply(self.weights_ho,hidden)
		output.add(self.bias_o)
		output.mapper(sigmoid)

		return output.toArray()

	def train(self,input_array,target_array):
		"""------FEED_FORWARD------"""
		inputs = Matrix.fromArray(input_array)

		hidden = Matrix.multiply(self.weights_ih,inputs)
		hidden.add(self.bias_h)
		#activation function
		# print("--------------------")
		# print("----------------")
		hidden.mapper(sigmoid)

		outputs = Matrix.multiply(self.weights_ho,hidden)
		outputs.add(self.bias_o)
		outputs.mapper(sigmoid)



		"""-----TRAINING-------"""

		#Convert array to Matrix object
		# outputs = Matrix.fromArray(outputs)
		targets = Matrix.fromArray(target_array)

		output_errors  = Matrix.subtract(targets, outputs)
		#Calculate output gradient
		gradients = Matrix.map(outputs,dsigmoid)
		gradients.scalar_multiply(output_errors)
		gradients.scalar_multiply(self.learning_rate)

		hiddden_T = Matrix.transpose(hidden)

		weights_ho_deltas = Matrix.multiply(gradients,hiddden_T)
		#Adjust the weight delatas
		self.weights_ho.add(weights_ho_deltas)
		#Adjust the bias
		self.bias_o.add(gradients)


		who_t = Matrix.transpose(self.weights_ho)
		#Calculate the hidden layer errors
		hidden_errors =  Matrix.multiply(who_t,output_errors)
		#Calculate hidden gradient
		hidden_gradient = Matrix.map(hidden,dsigmoid)
		hidden_gradient.scalar_multiply(hidden_errors)
		hidden_gradient.scalar_multiply(self.learning_rate)


		inputs_T =Matrix.transpose(inputs)
		weights_ih_deltas = Matrix.multiply(hidden_gradient,inputs_T)

		self.weights_ih.add(weights_ih_deltas)
		self.bias_h.add(hidden_gradient)

def sigmoid(*args):
		for x in args:
			return 1/(1+math.exp(-x))


def dsigmoid(*args):
		for x in args:
			return x * (1-x)
