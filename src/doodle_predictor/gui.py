import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageOps
import numpy as np
from .network import NeuralNetwork

class DoodleApp:
    def __init__(self, network: NeuralNetwork, labels: list[str]):
        self.network = network
        self.labels = labels
        
        self.root = tk.Tk()
        self.root.title("Doodle Predictor AI")
        
        # Canvas
        self.canvas_width = 400
        self.canvas_height = 400
        self.bg_color = "white"
        self.draw_color = "black"
        
        self.canvas = tk.Canvas(
            self.root, 
            bg=self.bg_color, 
            width=self.canvas_width, 
            height=self.canvas_height,
            cursor="cross"
        )
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Buttons Frame
        self.controls = tk.Frame(self.root)
        self.controls.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        self.btn_clear = tk.Button(self.controls, text="Clear", command=self.clear_canvas)
        self.btn_clear.pack(side=tk.LEFT, padx=10)

        self.btn_predict = tk.Button(self.controls, text="Predict", command=self.predict_doodle)
        self.btn_predict.pack(side=tk.RIGHT, padx=10)

        # Result Label
        self.lbl_result = tk.Label(self.root, text="Draw something!", font=("Arial", 16))
        self.lbl_result.pack(side=tk.BOTTOM, pady=10)

        # Drawing State
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), 255) # 'L' = grayscale, 255=white
        self.draw = ImageDraw.Draw(self.image)
        self.last_x, self.last_y = None, None

        # Bindings
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_coords)

    def paint(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            # Draw on canvas (visual)
            self.canvas.create_line(
                self.last_x, self.last_y, x, y, 
                width=15, fill=self.draw_color, capstyle=tk.ROUND, smooth=True
            )
            # Draw on PIL image (internal) - invert logic: 0=black
            self.draw.line(
                [self.last_x, self.last_y, x, y], 
                fill=0, width=15
            )
        self.last_x = x
        self.last_y = y

    def reset_coords(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.lbl_result.config(text="Draw something!")

    def predict_doodle(self):
        # 1. Resize to 28x28 (QuickDraw format)
        img_resized = self.image.resize((28, 28), Image.Resampling.LANCZOS)
        
        # 2. Invert (QuickDraw is white-on-black usually? Or black-on-white?)
        # QuickDraw dataset is usually 0=black (background), 255=white (stroke).
        # But my PIL image is 255=white (bg), 0=black (stroke).
        # So I need to invert it first: Stroke becomes 255 (white), BG becomes 0 (black).
        img_inverted = ImageOps.invert(img_resized)
        
        # 3. Convert to numpy array & normalize (0-1)
        arr = np.array(img_inverted, dtype=np.float32) / 255.0
        
        # 4. Flatten (28x28 -> 784)
        input_vec = arr.flatten()
        
        # 5. Predict
        output = self.network.predict(input_vec)
        prediction_idx = np.argmax(output)
        confidence = output[prediction_idx]
        
        label = self.labels[prediction_idx] if prediction_idx < len(self.labels) else "Unknown"
        self.lbl_result.config(text=f"I see a: {label} ({confidence:.1%})")

    def run(self):
        self.root.mainloop()
