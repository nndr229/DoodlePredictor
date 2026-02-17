import argparse
from pathlib import Path
import numpy as np
import sys
from .network import NeuralNetwork
from .data import DataLoader
from .trainer import Trainer
from .gui import DoodleApp

def main():
    parser = argparse.ArgumentParser(description="Doodle Predictor AI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Train Command
    train_parser = subparsers.add_parser("train", help="Train the neural network")
    train_parser.add_argument("--data", type=str, default="data", help="Directory containing .npy files")
    train_parser.add_argument("--output", type=str, default="model.pkl", help="Output model file")
    train_parser.add_argument("--epochs", type=int, default=5, help="Number of epochs")
    train_parser.add_argument("--limit", type=int, default=10000, help="Limit samples per class")

    # GUI Command
    gui_parser = subparsers.add_parser("gui", help="Launch the drawing interface")
    gui_parser.add_argument("--model", type=str, default="model.pkl", help="Path to trained model file")
    gui_parser.add_argument("--labels", type=str, help="Comma-separated list of labels (e.g. cat,dog,fish)")

    args = parser.parse_args()

    if args.command == "train":
        # ... (Loading data logic)
        
        # Train
        # ... (Training logic)
        
        # Save Model + Labels
        save_data = {
            'model': nn,
            'labels': class_names,
            'accuracy': accuracy
        }
        import pickle
        with open(args.output, 'wb') as f:
            pickle.dump(save_data, f)
        
        print(f"Training complete. Accuracy: {accuracy:.2%}")
        print(f"Saved model to {args.output}")

    elif args.command == "gui":
        model_path = Path(args.model)
        if not model_path.exists():
            print(f"Model file {model_path} not found. Run 'train' first.")
            sys.exit(1)

        print(f"Loading model from {model_path}...")
        import pickle
        with open(model_path, 'rb') as f:
            data = pickle.load(f)
            
        # Handle old format (just model) vs new format (dict)
        if isinstance(data, dict):
            network = data['model']
            labels = data.get('labels', [])
            if 'accuracy' in data:
                print(f"Model Accuracy: {data['accuracy']:.2%}")
        else:
            network = data
            labels = args.labels.split(",") if args.labels else [f"Label {i}" for i in range(network.output_nodes)]

        if not labels:
             print("Warning: No labels found in model file.")
             labels = [f"Label {i}" for i in range(network.output_nodes)]

        app = DoodleApp(network, labels)
        app.run()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
