# Assignment2_q2_t1
Import Libraries:

cv2 for image processing.
NumPy for numerical operations.
Matplotlib for displaying images.
Load Grayscale Image:

The image is loaded using cv2.imread() in grayscale mode. If the image is not loaded correctly, an error is raised.
Define Sobel Filters:

The Sobel X and Y filters are defined manually using NumPy arrays. These filters detect edges in the horizontal (X) and vertical (Y) directions, respectively.
Apply Sobel Filters:

The Sobel X filter is applied using cv2.filter2D(), which convolves the image with the filter to detect horizontal edges.
The Sobel Y filter is applied similarly to detect vertical edges.
Display Results:

The original image, the image filtered with the Sobel X filter, and the image filtered with the Sobel Y filter are displayed side by side using Matplotlib.
Output:

Three images are displayed: the original image, edges detected in the X-direction, and edges detected in the Y-direction.
This script is used for basic edge detection using the Sobel filter.
