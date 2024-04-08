import cv2

# giving image
image_path = 'pollen-lowcontrast.tif'
image = cv2.imread(image_path, 0)

# Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Displaying results
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
