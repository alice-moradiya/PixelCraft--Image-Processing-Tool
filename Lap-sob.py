import cv2
import numpy as np

# Load the image
image_path = 'baby.tif'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Applying Laplacian filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Applying Sobel filters
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Converting back to uint8
laplacian = np.uint8(np.absolute(laplacian))
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

# Displaying results
cv2.imshow('Original', image)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Sobel X Direction', sobelx)
cv2.imshow('Sobel Y Direction', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
