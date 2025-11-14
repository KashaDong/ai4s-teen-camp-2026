# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:11:59 2024

@author: NING MEI
"""

from PIL import Image
import os

# Define the source and destination directories
source_dir = "image_test_old"
dest_dir = "image_test"

# Create the destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Function to resize and save images
def resize_images(directory, size=(80, 60)):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            with Image.open(os.path.join(directory, filename)) as img:
                # Check if the image is 400x300
                if img.size == (400, 300):
                    img_resized = img.resize(size)
                    img_resized.save(os.path.join(dest_dir, filename))

# Resize and save the images
resize_images(source_dir)
len(os.listdir(dest_dir))  # Count the number of resized images to confirm