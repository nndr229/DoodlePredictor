# Doodle Predictor AI (v2.0)

A high-performance, vectorized neural network for predicting doodles. Built from scratch using NumPy (no TensorFlow/PyTorch required) but optimized for speed and readability.

## Features

- **Blazing Fast:** Fully vectorized operations using NumPy (100x faster than pure Python).
- **Clean Architecture:** Modular design (`network`, `trainer`, `data`, `gui`).
- **Interactive GUI:** Modern Tkinter interface for drawing and predicting.
- **Easy CLI:** Command-line tool for training and running.

## Installation

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/nndr229/DoodlePredictor.git
    cd DoodlePredictor
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Quick Start

### 1. Download Data
Download the QuickDraw dataset `.npy` files (e.g., `cat.npy`, `airplane.npy`) and place them in a `data/` folder.
[Google QuickDraw Dataset](https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap)

### 2. Train the Model
Train the network on your data. It automatically detects classes based on filenames.

```bash
python -m src.doodle_predictor train --data data/ --epochs 5 --output my_model.pkl
```

### 3. Run the GUI
Launch the drawing app to test your model.

```bash
python -m src.doodle_predictor gui --model my_model.pkl
```

## Advanced Features

### Pure Python Mode (Educational)
By default, Doodle Predictor uses NumPy for performance. However, for educational purposes, it includes a pure Python `Matrix` implementation (slow but easy to study).

To enable it, set `USE_NUMPY=false`:

```bash
USE_NUMPY=false python -m src.doodle_predictor train --data data/ --epochs 1
```

This is approximately 100x slower but demonstrates how Neural Networks work without libraries.

## Structure

*   `src/doodle_predictor/network.py`: The dispatcher (chooses between NumPy/Pure).
*   `src/doodle_predictor/network_numpy.py`: Fast implementation.
*   `src/doodle_predictor/network_pure.py`: Pure Python implementation using `matrix.py`.
*   `src/doodle_predictor/trainer.py`: Training loop and evaluation.
*   `src/doodle_predictor/data.py`: Data loading and preprocessing.
*   `src/doodle_predictor/gui.py`: The drawing interface.

## License
MIT
