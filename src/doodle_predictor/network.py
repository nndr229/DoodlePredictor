import os

# Dispatcher: Selects implementation based on environment variable
# USE_NUMPY=false will use the pure Python Matrix class (educational/legacy)
# USE_NUMPY=true (default) will use the optimized NumPy implementation

if os.environ.get("USE_NUMPY", "true").lower() == "false":
    try:
        from .network_pure import NeuralNetwork
        print("[DoodlePredictor] Using Pure Python Matrix implementation (Slow / Educational Mode)")
    except ImportError as e:
        print(f"[DoodlePredictor] Failed to load pure implementation: {e}")
        # Fallback?
        raise e
else:
    try:
        from .network_numpy import NeuralNetwork
        print("[DoodlePredictor] Using NumPy implementation (Fast / Production Mode)")
    except ImportError:
        # If numpy is missing but user didn't explicitly ask for pure, maybe warn?
        # But our package dependencies require numpy, so this should be fine.
        raise ImportError("NumPy is required for the default implementation. Install it or set USE_NUMPY=false.")
