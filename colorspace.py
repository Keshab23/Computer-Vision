import cv2
import numpy as np

#Origional Image
image = cv2.imread('nature.jpg').astype(np.float32) / 255
print('Shape:', image.shape)
print('Data type:', image.dtype)

#gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print('Converted to grayscale')
print('Shape:', gray.shape)
print('Data type:', gray.dtype)
cv2.imshow('gray', gray)
#cv2.waitKey()
#cv2.destroyAllWindows()

#hsv format
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print('Converted to HSV')
print('Shape:', hsv.shape)
print('Data type:', hsv.dtype)
cv2.imshow('hsv', hsv)
#cv2.waitKey()
#cv2.destroyAllWindows()

#Increase the Brightness and convert hsv to BGR
hsv[:, :, 2] *= 2
from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
print('Converted back to BGR from HSV')
print('Shape:', from_hsv.shape)
print('Data type:', from_hsv.dtype)
cv2.imshow('from_hsv', from_hsv)
cv2.waitKey()
cv2.destroyAllWindows()