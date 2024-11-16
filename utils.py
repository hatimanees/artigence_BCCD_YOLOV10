import os
import cv2
import numpy as np
import mxnet as mx
from albumentations import Compose, Rotate, RandomCrop
from PIL import Image

def convert_rec_to_images(rec_file, save_dir, prefix="train"):
    """
    Convert .rec file to individual images and labels for YOLO.
    Args:
        rec_file (str): Path to .rec file (e.g., train.rec or val.rec)
        save_dir (str): Directory where images and labels are saved
        prefix (str): Prefix for filenames (e.g., "train" or "val")
    """
    image_dir = os.path.join(save_dir, "images")
    label_dir = os.path.join(save_dir, "labels")
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)

    record = mx.recordio.MXIndexedRecordIO(rec_file + '.idx', rec_file, 'r')
    idx = 0

    while True:
        item = record.read()
        if item is None:
            break

        header, img = mx.recordio.unpack_img(item)

        # Save image
        img_name = f"{prefix}_{idx}.jpg"
        img_path = os.path.join(image_dir, img_name)
        cv2.imwrite(img_path, img)

        # Save label
        label_path = os.path.join(label_dir, f"{prefix}_{idx}.txt")
        with open(label_path, "w") as f:
            if isinstance(header.label, (list, np.ndarray)):
                for label in header.label:
                    class_id, x_center, y_center, width, height = label
                    f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
            else:
                class_id, x_center, y_center, width, height = header.label
                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

        idx += 1

def augment_image(image):
    """
    Apply data augmentation to an image.
    Args:
        image (PIL.Image): Image to augment
    Returns:
        PIL.Image: Augmented image
    """
    augment = Compose([Rotate(limit=30, p=0.5), RandomCrop(224, 224, p=0.5)])
    image = np.array(image)
    augmented = augment(image=image)
    return Image.fromarray(augmented["image"])
