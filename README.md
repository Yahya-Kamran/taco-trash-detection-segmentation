# ♻️ Trash Detection & Segmentation (TACO)

[![Framework](https://img.shields.io/badge/Framework-PyTorch-red.svg)](#)
[![Model](https://img.shields.io/badge/Model-YOLOv8_%7C_U--Net-green.svg)](#)
[![Dataset](https://img.shields.io/badge/Dataset-TACO-blue.svg)](#)

> A dual-pipeline computer vision system designed to detect and segment environmental waste in the wild.

## 📖 Overview
Tackling the global waste problem requires advanced automation. This project leverages the **TACO (Trash Annotations in Context)** dataset to build two distinct vision architectures: 
1. **YOLOv8** for high-speed, real-time object detection (bounding boxes).
2. **U-Net** for highly precise, pixel-wise instance segmentation (masks).

## ✨ Key Features
- **Dual Architecture Implementation**: Provides both detection and segmentation pipelines for comparison.
- **Custom Evaluation Metrics**: Includes a dedicated `cv_utils.py` module for calculating Intersection over Union (IoU) and mean Average Precision (mAP).
- **Data Augmentation**: Robust preprocessing to handle the high variance in real-world trash photos (lighting, occlusion).
- **Visual Analytics**: Side-by-side comparative plotting of Ground Truth vs. Predicted Masks.

## 📁 Repository Structure
```text
.
├── taco_yolo_unet_pipeline.ipynb   # Main pipeline notebook (Training & Inference)
├── cv_utils.py                     # Custom metrics and visualization utilities
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🚀 Setup & Usage
1. Clone the repository and navigate to the directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch Jupyter Notebook or Jupyter Lab to explore the pipeline:
   ```bash
   jupyter notebook taco_yolo_unet_pipeline.ipynb
   ```
