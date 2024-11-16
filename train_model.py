import subprocess

def train_model(model_path, data_file, project_dir):
    """Trains the YOLO model."""
    print("Starting model training...")
    subprocess.run([
        "yolo", "task=detect", "mode=train", "epochs=100", "batch=16", "plots=True",
        f"model={model_path}", f"data={data_file}", f"project={project_dir}", "name=custom_model"
    ], check=True)
