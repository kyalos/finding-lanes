import cv2
import numpy as np


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def regionOfInterest(image):
    height = image.shape[0]
    polygons = np.array([[(200, height), (1100, height), (500, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask


image = cv2.imread('test_image.jpg')

laneImage = np.copy(image)
canny = canny(laneImage)
cv2.imshow("results", regionOfInterest(canny))
cv2.waitKey(0)
