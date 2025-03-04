import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a grayscale image (replace 'sample.jpg' with your image path)
image = cv2.imread('C:\Users\91814\Pictures\SavedPictures\popo.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded properly
if image is None:
    raise ValueError("Image not loaded. Please check the path and try again.")

# Define the Sobel X and Y filters
sobel_x_filter = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

sobel_y_filter = np.array([[-1, -2, -1],
                           [ 0,  0,  0],
                           [ 1,  2,  1]])

# Apply the Sobel X filter
sobel_x = cv2.filter2D(image, cv2.CV_64F, sobel_x_filter)

# Apply the Sobel Y filter
sobel_y = cv2.filter2D(image, cv2.CV_64F, sobel_y_filter)

# Display the original and the filtered images
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Sobel X image
plt.subplot(1, 3, 2)
plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel X')
plt.axis('off')

# Sobel Y image
plt.subplot(1, 3, 3)
plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel Y')
plt.axis('off')

# Show the plots
plt.tight_layout()
plt.show()
