
Project Overview

This project involves working with a dataset of images and their corresponding labels. The objective was to preprocess the data, convert the labels to YOLO format, split the data into training and validation sets, and train a YOLOv8x model on the data. Post-training, the model was optimized using OpenVINO for faster inference. Below is a step-by-step guide on the process, including scripts used at each stage.
 Steps Involved

1. Dataset Acquisition and Label Conversion:
   We received a dataset of images with their corresponding labels.
   The labels were converted to YOLO format and saved as `.txt` files.

2. Separating Images Based on Annotations:
   Images without annotations were moved to a separate folder.
   Images with annotations were moved to another folder.

3. Splitting Data into Training and Validation Sets:
   The images with annotations were split into training and validation sets.
   A YAML file was created containing the paths to the training and validation data, along with the class names for the objects to be detected.

4. Creating Dataset Archive:**
   The training and validation data were archived into a ZIP folder named `dataset.zip`.
   This ZIP folder, including the YAML file, was uploaded to Google Drive.

5. Model Training:
   The YOLOv8x model was used to train on the specified classes using Google Colab.
   When training on the GPU was slow, the model was optimized using OpenVINO.

6. Inference:
   The trained model was downloaded and used for inference.
   Three video files (`test_video1.mp4`, `test_video2.mp4`, `test_video3.mp4`) were processed, and the results   were saved as `output_video1.mp4`, `output_video2.mp4`, and `output_video3.mp4`.

Scripts Used

1. yoloLabelConversion.py:
   This script converts the labels from their original format to YOLO format and saves them as `.txt` files.

2. seperate.py:
   This script separates images into folders based on whether they have annotations or not.

3. data_splitting.py:
   This script splits the images with annotations into training and validation sets and creates the necessary directory structure.

4. inference.py:
   This script performs inference using the trained YOLOv8x model on the provided video files and saves the output.

OpenVINO Optimization

OpenVINO is a toolkit for optimizing deep learning models for faster inference on Intel hardware. It was used to enhance the inference speed of the trained YOLOv8x model, allowing for efficient real-time video processing.


Scripts

1. yoloLabelConversion.py:
   Converts labels to YOLO format.
   Saves labels as `.txt` files.

2. seperate.py:
   Checks for the existence of labels for each image.
   Moves images without annotations to a `without_annotations` folder.
   Moves images with annotations to a `with_annotations` folder.

3. data_splitting.py:
   Reads the images with annotations.
   Splits the data into training and validation sets.
   Moves the files to respective folders.

4. inference.py:
   Loads the trained YOLOv8x model.
   Processes video files for object detection.
   Saves the output videos with detections.

By following this process, we effectively managed the dataset, trained a YOLO model, optimized it for performance, and used it for inference on video files. The provided scripts automate these steps, ensuring a streamlined workflow from data preprocessing to model inference.