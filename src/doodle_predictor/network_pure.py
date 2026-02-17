from typing import List, Union
import math
from .matrix import Matrix

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def dsigmoid(y):
    # Derivative of sigmoid in terms of output y
    return y * (1 - y)

class NeuralNetwork:
    """
    A pure Python implementation of a Feed Forward Neural Network using Matrix operations.
    Use this for educational purposes or when NumPy is unavailable.
    """
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate=0.1):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate

        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

    def predict(self, input_array: Union[List[float], 'numpy.ndarray']) -> List[float]:
        # Convert numpy input to list if needed
        if hasattr(input_array, 'tolist'):
            input_array = input_array.tolist()
            
        # Generating the hidden outputs
        inputs = Matrix.fromArray(input_array)
        hidden = Matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        # activation function
        hidden.mapper(sigmoid)

        output = Matrix.multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.mapper(sigmoid)

        return output.toArray()

    def train(self, input_array: Union[List[float], 'numpy.ndarray'], target_array: Union[List[float], 'numpy.ndarray']):
        if hasattr(input_array, 'tolist'):
            input_array = input_array.tolist()
        if hasattr(target_array, 'tolist'):
            target_array = target_array.tolist()

        inputs = Matrix.fromArray(input_array)
        
        # Feed Forward
        hidden = Matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.mapper(sigmoid)

        outputs = Matrix.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.mapper(sigmoid)

        # Backpropagation
        targets = Matrix.fromArray(target_array)
        
        # Output Errors
        output_errors = Matrix.subtract(targets, outputs)
        
        # Output Gradient
        gradients = Matrix.map(outputs, dsigmoid)
        gradients.scalar_multiply(output_errors)
        gradients.scalar_multiply(self.learning_rate)

        # Hidden->Output Deltas
        hidden_T = Matrix.transpose(hidden)
        weights_ho_deltas = Matrix.multiply(gradients, hidden_T)

        # Update Weights/Biases
        self.weights_ho.add(weights_ho_deltas)
        self.bias_o.add(gradients)

        # Hidden Errors
        who_t = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.multiply(who_t, output_errors)

        # Hidden Gradient
        hidden_gradient = Matrix.map(hidden, dsigmoid)
        hidden_gradient.scalar_multiply(hidden_errors)
        hidden_gradient.scalar_multiply(self.learning_rate)

        # Input->Hidden Deltas
        inputs_T = Matrix.transpose(inputs)
        weights_ih_deltas = Matrix.multiply(hidden_gradient, inputs_T)

        # Update Weights/Biases
        self.weights_ih.add(weights_ih_deltas)
        self.bias_h.add(hidden_gradient)
