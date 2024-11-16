import os
from repo_manager import clone_repo
from env_manager import install_requirements
from weights_manager import download_weights
from train_model import train_model
from predict_model import make_predictions
from utils import create_dir_if_not_exists

# Constants for paths
weights_dir = os.path.join(os.getcwd(), "weights")
project_dir = "C:/Users/HP"
data_file = "C:/Users/HP/custom_dataset.yaml"
image_file = "C:/Users/HP/BCCD.yolov11/train/images/BloodImage_00001_jpg.rf.d702f2b1212a2ed897b5607804109acf.jpg"
output_dir = "C:/Users/HP/run"
repo_url = "https://github.com/THU-MIG/yolov10.git"
repo_dir = "yolov10"

# URLs of the weight files
urls = [
    "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt",
    "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10s.pt",
    "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10m.pt",
    "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10b.pt",
    "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10x.pt",
    "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10l.pt"
]


# Main workflow
def main():
    # Clone the repo
    clone_repo(repo_url, repo_dir)

    # Install requirements
    install_requirements()

    # Download weights
    download_weights(weights_dir, urls)

    # Train the model
    model_path = os.path.join(weights_dir, "yolov10n.pt")
    train_model(model_path, data_file, project_dir)


if __name__ == "__main__":
    main()
