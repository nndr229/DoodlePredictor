from typing import List, Callable, Optional, Union, Tuple
import numpy as np

# Activation Functions
def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))

def dsigmoid(y: np.ndarray) -> np.ndarray:
    # Derivative of sigmoid in terms of the output y
    return y * (1 - y)

class NeuralNetwork:
    """
    A simple Feed Forward Neural Network with one hidden layer.
    Optimized with NumPy for vectorized operations.
    """
    def __init__(
        self, 
        input_nodes: int, 
        hidden_nodes: int, 
        output_nodes: int, 
        learning_rate: float = 0.1
    ):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate

        # Initialize weights with random values between -1 and 1
        # Shape: (hidden, input)
        self.weights_ih = np.random.uniform(-1, 1, (self.hidden_nodes, self.input_nodes))
        # Shape: (output, hidden)
        self.weights_ho = np.random.uniform(-1, 1, (self.output_nodes, self.hidden_nodes))

        # Initialize biases
        # Shape: (hidden, 1)
        self.bias_h = np.random.uniform(-1, 1, (self.hidden_nodes, 1))
        # Shape: (output, 1)
        self.bias_o = np.random.uniform(-1, 1, (self.output_nodes, 1))

    def predict(self, input_array: Union[List[float], np.ndarray]) -> np.ndarray:
        """
        Feed forward the inputs through the network to get predictions.
        """
        # Convert input to column vector (n, 1)
        inputs = np.array(input_array).reshape(-1, 1)

        # Hidden Layer
        hidden = np.dot(self.weights_ih, inputs)
        hidden += self.bias_h
        hidden = sigmoid(hidden)

        # Output Layer
        output = np.dot(self.weights_ho, hidden)
        output += self.bias_o
        output = sigmoid(output)

        return output.flatten()

    def train(self, input_array: Union[List[float], np.ndarray], target_array: Union[List[float], np.ndarray]) -> None:
        """
        Train the network for one iteration (stochastic gradient descent).
        """
        # 1. Feed Forward
        inputs = np.array(input_array).reshape(-1, 1)
        targets = np.array(target_array).reshape(-1, 1)

        # Hidden Layer
        hidden_raw = np.dot(self.weights_ih, inputs) + self.bias_h
        hidden = sigmoid(hidden_raw)

        # Output Layer
        output_raw = np.dot(self.weights_ho, hidden) + self.bias_o
        outputs = sigmoid(output_raw)

        # 2. Backpropagation
        
        # Output Errors: target - output
        output_errors = targets - outputs

        # Calculate Output Gradients
        # gradient = lr * error * dsigmoid(output)
        gradients = dsigmoid(outputs)
        gradients *= output_errors
        gradients *= self.learning_rate

        # Calculate Hidden->Output Weight Deltas
        # delta_who = gradient * hidden_T
        hidden_T = hidden.T
        weights_ho_deltas = np.dot(gradients, hidden_T)

        # Update Hidden->Output Weights & Biases
        self.weights_ho += weights_ho_deltas
        self.bias_o += gradients

        # Hidden Layer Errors
        # hidden_error = who_T * output_error
        who_T = self.weights_ho.T
        hidden_errors = np.dot(who_T, output_errors)

        # Calculate Hidden Gradients
        hidden_gradient = dsigmoid(hidden)
        hidden_gradient *= hidden_errors
        hidden_gradient *= self.learning_rate

        # Calculate Input->Hidden Weight Deltas
        inputs_T = inputs.T
        weights_ih_deltas = np.dot(hidden_gradient, inputs_T)

        # Update Input->Hidden Weights & Biases
        self.weights_ih += weights_ih_deltas
        self.bias_h += hidden_gradient
