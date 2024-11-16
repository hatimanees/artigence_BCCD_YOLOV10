# Object Detection Web App

This project is an object detection app developed using YOLO on the BCCD dataset. The app allows users to upload images to detect objects (blood cells) and view predictions.

## Project Structure
- `app.py`: Main application file (Gradio or Streamlit)
- `model.py`: Model loading, training, and inference functions
- `utils.py`: Utility functions (data augmentation, .rec extraction)
- `BCCD.yaml`: Dataset configuration for YOLO
- `requirements.txt`: List of dependencies
- `train.rec` / `val.rec`: Dataset files
- `train_data/`, `val_data/`: Extracted images and labels for training and validation

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd object-detection-app
