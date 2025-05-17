# Manual Image Matching and Stitching

This project demonstrates an end-to-end image stitching pipeline with an optional interactive point selection tool. Users can either run the automated pipeline or manually define keypoint correspondences between two images.

## 🧩 Project Components

### 📘 `image_stitch_implementation.ipynb`
A complete implementation of the image stitching algorithm using:
- Feature detection (hand pick points)
- Kabsch-Umeyama Algorithm
- Keypoint matching
- Homography estimation
- Warping and blending

This notebook walks through the theoretical and practical steps of stitching two overlapping images together into a panorama.

### 🖱️ `ClickMatchVisualizer.py`
An interactive tool to manually select corresponding points between two images.

**Features:**
- Load your own stereo or overlapping image pair
- Click alternately between the two images to define matches
- Saves the correspondences to a `.json` file

**Usage:**
```bash
python ClickMatchVisualizer.py
````

Make sure to update the image paths in the script:

```python
img1_path = "bonus/left_pc.jpg"
img2_path = "bonus/right_pc.jpg"
output_json = "bonus/correspondences"
```

The final JSON will look like:

```json
[
  {
    "img1_xy": [x1, y1],
    "img2_xy": [x2, y2]
  },
  ...
]
```

## 📁 Directory Structure

```
manual-image-matching-and-stitching/
├── bonus/
│   ├── custom_image1.jpg
│   ├── custom_image2.jpg
│   └── correspondences (JSON output)
├── dataset1
├── dataset2
├── ClickMatchVisualizer.py
├── image_stitch_implementation.ipynb
└── README.md
```

## ✅ Requirements

* Python 3.x
* OpenCV (`cv2`)
* Jupyter Notebook

Install dependencies using:

```bash
pip install opencv-python jupyter
```

## 🚀 How to Run

1. Open the notebook:

```bash
jupyter notebook image_stitch_implementation.ipynb
```

2. (Optional) Use `ClickMatchVisualizer.py` to define your own correspondences and feed that data into the notebook.

## 📸 Example Use Cases

* Educational demos for computer vision
* Manual stitching of historical or misaligned images
* Visual debugging of keypoint correspondence algorithms

## 👨‍💻 Author

Emre Çağrı Dalcı

---
