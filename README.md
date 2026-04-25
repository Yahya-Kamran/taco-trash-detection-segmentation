# Trash Detection and Segmentation using YOLO and U-Net

## Overview
This project applies computer vision techniques to the TACO dataset for:

- Object detection using YOLO
- Image segmentation using U-Net

The goal is to explore detection and segmentation approaches for real-world trash recognition.

## Components

### YOLO Detection
- Converts dataset annotations into YOLO format
- Trains an object detection model
- Evaluates detection performance

### U-Net Segmentation
- Performs pixel-wise segmentation
- Trains a U-Net model on trash masks
- Evaluates segmentation results

## Dataset
- TACO (Trash Annotations in Context)

## Technologies Used
- Python
- PyTorch
- Ultralytics YOLO
- OpenCV
- NumPy
- Matplotlib
