import cv2
import numpy as np
image = cv2.imread('nature.jpg', 0).astype(np.float32) / 255

#Apply per-element exponentiation using the specified exponent value, gamma :
gamma = 0.5
corrected_image = np.power(image, gamma)

#Display the source and result images:
cv2.imshow('image', image)
cv2.imshow('corrected_image', corrected_image)
cv2.waitKey()
cv2.destroyAllWindows()