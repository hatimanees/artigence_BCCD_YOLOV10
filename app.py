import torch
from PIL import Image
import numpy as np
import streamlit as st
from ultralytics import YOLO

# Load YOLOv10 model
model = YOLO('checkpoints/best.pt')  # Load the pre-trained model

# Streamlit App
st.title("YOLO Object Detection with Confidence Threshold")

st.sidebar.title("Options")
st.sidebar.markdown("Upload an image to detect objects.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load the image
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform inference with a confidence threshold of 0.25
    st.write("Detecting objects with confidence threshold of 0.25...")
    results = model.predict(source=image, conf=0.25, save=False)  # Directly pass PIL image

    # Annotate and display the image
    annotated_image = results[0].plot()  # Get annotated image with bounding boxes
    st.image(annotated_image, caption="Detected Objects", use_column_width=True)

    # Show raw predictions
    st.write("Detection Results:")
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)  # Convert to Python int
            confidence = float(box.conf)  # Convert to Python float
            bbox = box.xyxy.tolist()  # Bounding box coordinates as a list

            st.write(
                f"Class: {class_id}, Confidence: {confidence:.2f}, Box: {bbox}"
            )

st.sidebar.info("Developed using YOLO")
