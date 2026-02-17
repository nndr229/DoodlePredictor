import numpy as np
from typing import List, Tuple
import pickle
from pathlib import Path
from .network import NeuralNetwork

class Trainer:
    def __init__(self, network: NeuralNetwork):
        self.network = network

    def train(
        self, 
        X_train: np.ndarray, 
        y_train: np.ndarray, 
        epochs: int = 1, 
        batch_size: int = 1 # SGD default
    ) -> None:
        """
        Train the network on the provided data.
        """
        print(f"Training on {len(X_train)} samples for {epochs} epochs...")
        
        # Determine number of classes from y_train (assuming 0..N-1 labels)
        num_classes = self.network.output_nodes
        
        for epoch in range(epochs):
            indices = np.arange(len(X_train))
            np.random.shuffle(indices)
            
            correct = 0
            
            for i in indices:
                input_vec = X_train[i]
                label = y_train[i]
                
                # One-hot encode target
                target_vec = np.zeros(num_classes)
                target_vec[int(label)] = 1.0
                
                # Train step
                self.network.train(input_vec, target_vec)
                
                # Check accuracy roughly every 1000 steps or just track loss?
                # For simplicity, let's just train.
                
            print(f"Epoch {epoch+1}/{epochs} complete.")

    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> float:
        """
        Evaluate accuracy on test set.
        """
        correct = 0
        total = len(X_test)
        
        for i in range(total):
            prediction = self.network.predict(X_test[i])
            predicted_class = np.argmax(prediction)
            
            if predicted_class == y_test[i]:
                correct += 1
                
        accuracy = correct / total
        print(f"Test Accuracy: {accuracy:.2%}")
        return accuracy

    def save_model(self, path: str):
        """Save the network weights/biases."""
        with open(path, 'wb') as f:
            pickle.dump(self.network, f)
        print(f"Model saved to {path}")

    @staticmethod
    def load_model(path: str) -> NeuralNetwork:
        """Load a trained network."""
        with open(path, 'rb') as f:
            return pickle.load(f)
