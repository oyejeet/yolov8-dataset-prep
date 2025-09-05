# 🖼️ Simple Image Downloader for YOLOv8

This repository contains a Python script to download images from the internet using the [`simple-image-download`] package.  
The images can later be cleaned, annotated, and used to prepare datasets for training YOLOv8 object detection models.  

---

## ⚙️ Setup

### 1. Create Virtual Environment

**Option A: Using `venv`**

python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

**Option A: Using `Anaconda`**

conda create -n yolov8 python=3.12.7
conda activate yolov8

### 2. Install Dependencies

pip install simple-image-download

### 3. Run the Script

python image_download.py