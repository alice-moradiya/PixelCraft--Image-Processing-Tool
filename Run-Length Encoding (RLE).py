import cv2
import numpy as np

def encode_rle(img):
    """Encodes a grayscale image with Run-Length Encoding (RLE)."""
    flat_img = img.flatten()
    result = []
    prev_pixel = flat_img[0]
    count = 1

    for pixel in flat_img[1:]:
        if pixel == prev_pixel:
            count += 1
        else:
            result.append((prev_pixel, count))
            prev_pixel = pixel
            count = 1
    result.append((prev_pixel, count))
    return result

image_path = 'pollen-lowcontrast.tif'

# Loading the image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# checking if the image is loaded properly
if image is None:
    print("Error loading image")
else:
    # Encode the image using RLE
    encoded_rle = encode_rle(image)
    print(encoded_rle)
