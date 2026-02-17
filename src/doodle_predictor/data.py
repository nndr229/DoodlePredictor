import numpy as np
from sklearn.model_selection import train_test_split
from pathlib import Path
from typing import Tuple, List, Optional
import h5py

class DataLoader:
    """
    Handles loading and preprocessing of QuickDraw dataset files (.npy format).
    """
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        
    def load_raw_files(self, limit_per_class: int = 10000) -> Tuple[np.ndarray, np.ndarray, List[str]]:
        """
        Loads all .npy files in the data directory.
        Returns (X, y, class_names).
        """
        if not self.data_dir.exists():
            raise FileNotFoundError(f"Data directory {self.data_dir} not found.")

        npy_files = list(self.data_dir.glob("*.npy"))
        if not npy_files:
            raise FileNotFoundError(f"No .npy files found in {self.data_dir}")

        X_list = []
        y_list = []
        class_names = []

        for i, file_path in enumerate(npy_files):
            class_name = file_path.stem  # e.g., "cat.npy" -> "cat"
            class_names.append(class_name)
            
            print(f"Loading {class_name}...")
            # Load data
            data = np.load(file_path)
            
            # Limit size to save memory/time
            if limit_per_class and len(data) > limit_per_class:
                data = data[:limit_per_class]
                
            # Create labels
            labels = np.full(len(data), i)
            
            X_list.append(data)
            y_list.append(labels)

        # Concatenate all classes
        X = np.concatenate(X_list, axis=0)
        y = np.concatenate(y_list, axis=0)
        
        return X, y, class_names

    def preprocess(self, X: np.ndarray, normalize: bool = True) -> np.ndarray:
        """
        Normalize pixel values to 0-1 range.
        """
        if normalize:
            X = X.astype("float32") / 255.0
        return X

    def split_data(
        self, 
        X: np.ndarray, 
        y: np.ndarray, 
        test_size: float = 0.2, 
        random_state: int = 42
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Split into train and test sets.
        """
        return train_test_split(X, y, test_size=test_size, random_state=random_state)

    def save_h5(self, X_train, X_test, y_train, y_test, output_dir: str = "."):
        """
        Save processed datasets to HDF5 format.
        """
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        
        with h5py.File(out_path / "doodle_data.h5", "w") as hf:
            hf.create_dataset("x_train", data=X_train)
            hf.create_dataset("x_test", data=X_test)
            hf.create_dataset("y_train", data=y_train)
            hf.create_dataset("y_test", data=y_test)
            
        print(f"Saved dataset to {out_path / 'doodle_data.h5'}")
