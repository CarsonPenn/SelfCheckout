import os
import cv2
from runModel import *  # or wherever your runModel function lives

# Folder containing your test images/videos
test_dir = "test_files/"

# Supported file types (you can add more)
supported_exts = ('.jpg', '.jpeg', '.png', '.mp4', '.mov', '.avi')

# Loop through all files in the folder
for filename in os.listdir(test_dir):
    filepath = (test_dir + filename)
    # img = cv2.imread(filepath)

    # if img is None:
    #     print("❌ OpenCV failed to load the image.")
    # else:
    #     print("✅ Image loaded fine.")
    if filename.lower().endswith(supported_exts):
        filepath = (test_dir + filename)
        print(f"🚀 Running YOLO on: {filepath}")
        runModel(source=filepath)
