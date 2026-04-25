import numpy as np
import matplotlib.pyplot as plt
import cv2

def calculate_iou(mask1, mask2):
    \"\"\"Intersection over Union calculation for segmentation masks.\"\"\"
    intersection = np.logical_and(mask1, mask2)
    union = np.logical_or(mask1, mask2)
    iou_score = np.sum(intersection) / np.sum(union)
    return iou_score

def plot_side_by_side(image, mask_gt, mask_pred, title=\"Segmentation Results\"):
    \"\"\"Visualizes original image, ground truth, and prediction.\"\"\"
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title(\"Original Image\")
    plt.axis(\"off\")
    
    plt.subplot(1, 3, 2)
    plt.imshow(mask_gt, cmap=\"gray\")
    plt.title(\"Ground Truth\")
    plt.axis(\"off\")
    
    plt.subplot(1, 3, 3)
    plt.imshow(mask_pred, cmap=\"jet\", alpha=0.7)
    plt.title(\"Prediction Overlay\")
    plt.axis(\"off\")
    
    plt.suptitle(title)
    plt.show()

def draw_bboxes(image, bboxes, labels):
    \"\"\"Draws bounding boxes with labels on the image.\"\"\"
    img_copy = image.copy()
    for bbox, label in zip(bboxes, labels):
        x1, y1, x2, y2 = bbox
        cv2.rectangle(img_copy, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(img_copy, label, (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return img_copy

if __name__ == \"__main__\":
    print(\"CV Utilities module initialized.\")
