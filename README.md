Here's a `README.md` template for your project, leaving space for the specific metrics and curves you mentioned (Confusion Matrix, F1 Curve, etc.). You can fill in the placeholders once you have the results.

```markdown
# YOLOv10 Custom Object Detection

This repository implements a custom object detection pipeline using the YOLOv10 model. The pipeline includes training the model on a custom dataset and making predictions on new images. This repository provides a modular and easily extensible code structure to handle the entire process, from repository cloning to training, prediction, and evaluation.

## Project Structure

```plaintext
.
├── main.py                # Entry point for the program
├── repo_manager.py        # Handles git operations
├── env_manager.py         # Handles environment setup (e.g., pip install)
├── weights_manager.py     # Manages downloading the weights
├── train_model.py         # Model training logic
├── predict_model.py       # Model prediction logic
└── utils.py               # General utility functions (e.g., path handling)
```

## Example Input
![BloodImage_00001_jpg rf d702f2b1212a2ed897b5607804109acf](https://github.com/user-attachments/assets/d7c3c90f-6c40-4ec0-9488-38d169e43390)


## Example Output
![BloodImage_00001_jpg rf d702f2b1212a2ed897b5607804109acf](https://github.com/user-attachments/assets/27ddcac0-59a7-4739-9709-901b7ad17af1)

## Installation

To use the code in this repository, follow the steps below:

### 1. Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/yolov10.git
cd yolov10
```

### 2. Install Dependencies
The repository requires Python and several packages for the YOLOv10 implementation. Install the necessary dependencies by running:

```bash
pip install .
```

### 3. Download Pre-trained Weights
To download the pre-trained weights for the YOLOv10 models, run the following script. It will download weights for different model sizes (`n`, `s`, `m`, `b`, `x`, `l`):

```bash
python download_weights.py
```

### 4. Train the Model
To train the model on your custom dataset, ensure your dataset YAML file (`custom_dataset.yaml`) is set up correctly. Then, run the following command:

```bash
python train_model.py --data custom_dataset.yaml --epochs 100 --batch-size 16 --model yolov10n.pt
```

This will train the model using the `yolov10n.pt` weights as a starting point.

### 5. Make Predictions
Once the model is trained, you can make predictions on new images by running:

```bash
python predict_model.py --model "path/to/best_model.pt" --image "path/to/test_image.jpg" --output-dir "path/to/output_dir"
```

## Evaluation

The performance of the model can be evaluated using various metrics and plots. After training the model, you can generate the following evaluation metrics:

### Confusion Matrix
![confusion_matrix_normalized](https://github.com/user-attachments/assets/23f41f08-497b-4007-81b1-a3ddf4318ba9)


### F1 Curve
![F1_curve](https://github.com/user-attachments/assets/448281da-6d91-4320-b742-9dbf181f2085)


### Labels
![labels_correlogram](https://github.com/user-attachments/assets/4f7e24f9-49b4-4169-8a9b-c4f83ac8ba20)


### Precision-Recall Curve (P Curve)
![P_curve](https://github.com/user-attachments/assets/5962d022-96b4-4d71-a384-3c607c88bda2)


### Precision-Recall Curve (PR Curve)
![PR_curve](https://github.com/user-attachments/assets/dd23738c-df32-4f59-8d61-59906f151f9e)


### Recall Curve (R Curve)
![R_curve](https://github.com/user-attachments/assets/e560ba21-bfe1-437d-9882-872675710b1c)


### Results
![results](https://github.com/user-attachments/assets/ab309a62-162d-407f-9f05-acbf5d235b04)


## Usage

After running the training and prediction scripts, you will be able to evaluate the results and view the performance of your custom-trained YOLOv10 model. You can also visualize the evaluation metrics (such as confusion matrix and curves) to get a better understanding of the model's performance.

### Example usage for training:
```bash
python train_model.py --data path/to/custom_dataset.yaml --epochs 50 --batch-size 16 --model yolov10m.pt
```

### Example usage for prediction:
```bash
python predict_model.py --model "path/to/custom_model/weights/best.pt" --image "path/to/test_image.jpg" --output-dir "path/to/output_dir"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- YOLOv10 model from [THU-MIG](https://github.com/THU-MIG/yolov10).
- The dataset used in this project is customized for object detection tasks.

---

### Note:
- Don't forget to replace placeholders like `path/to/your_model` and `path/to/your_image` with actual paths on your local machine.
- The evaluation metrics (Confusion Matrix, Precision-Recall Curves, etc.) will be generated after the training process and can be found in the logs or output directory.
```

### How to Update the ReadMe:

1. **Confusion Matrix**:  
   You can generate and insert the confusion matrix from your model's evaluation.

2. **F1 Curve**:  
   After calculating the F1 scores, plot the curve and insert the image of the plot.

3. **Labels**:  
   If you have specific class labels for your dataset, insert those here.

4. **Precision-Recall Curve (P Curve)**:  
   Plot the precision-recall curve and update the file with the results.

5. **PR Curve**:  
   Plot the precision-recall curve and insert it similarly.

6. **Recall Curve (R Curve)**:  
   Plot the recall curve and insert it as well.

7. **Results**:  
   After completing training and predictions, summarize the overall performance metrics (accuracy, precision, recall, F1-score, etc.) for the final results.

This structure should give you a good starting point, and you can fill in the placeholders once you have the metrics and results from training and evaluation!
