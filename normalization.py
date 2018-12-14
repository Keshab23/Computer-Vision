import cv2
import numpy as np

#Load an image and convert it to one with floating-point elements in range [0,1] :
image = cv2.imread('nature.jpg').astype(np.float32) / 255
cv2.imshow('Origional Image',image)
#Subtract the mean value from each image pixel to get a zero-mean matrix. 
#Then,divide each pixel value by its standard deviation to have a unit-variance matrix:
image -= image.mean()
image /= image.std()
cv2.imshow('Normalized Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()