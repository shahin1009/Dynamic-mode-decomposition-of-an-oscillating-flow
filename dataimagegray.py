import cv2
import numpy as np
import glob

# Load a list of images
images = [cv2.imread(file) for file in glob.glob("*.png")]

# Convert each image into a 1D array of pixel values
data = [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).flatten() for image in images]

# Stack the 1D arrays as columns in a 2D numpy array
data = np.column_stack(data)

# Perform some operation on the data, such as mean subtraction
mean = np.mean(data, axis=1, keepdims=True)
data = data - mean

# Save the processed data to a file
np.save("processed_data.npy", data)
