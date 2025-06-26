# Image Segmentation

This project implements basic image segmentation techniques using Python and OpenCV. It covers both thresholding with noise and region-based segmentation.

## Contents

1. **Otsu's Thresholding with Gaussian Noise** – `otsu_thresholding.py`
2. **Region Growing Segmentation** – `region_growing.py`

---

## 1. Otsu’s Thresholding with Gaussian Noise

- A synthetic grayscale image with two object regions and a background is generated.
- Gaussian noise is added to simulate real-world image degradation.
- Otsu’s thresholding is applied to separate foreground objects from the background.

### To Run:
```bash
python otsu_thresholding.py
```

---

## 2. Region Growing Segmentation

- Implements a pixel-based region-growing algorithm.
- Starts from a set of user-defined seed points and recursively includes neighboring pixels.
- Pixels are added to a region if their intensity is within a defined threshold of the respective seed's value.

### To Run:
```bash
python region_growing.py
```

You can modify the seed point or threshold value in the script to observe different results.

---

## Dependencies

Install required libraries with:
```bash
pip install opencv-python matplotlib numpy
```

---

## Output

The scripts display the original image, intermediate, and segmented results using matplotlib visualizations.

---