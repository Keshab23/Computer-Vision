import cv2
import numpy as np
import matplotlib.pyplot as plt

#Load the test binary image:
image = cv2.imread('bnw.png', 0)

#Find the external and internal contours. Organize them into a two-level hierarchy:
_,contours, hierarchy = cv2.findContours(image, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

#Prepare the external contour binary mask:
image_external = np.zeros(image.shape, image.dtype)
for i in range(len(contours)):
	if hierarchy[0][i][3] == -1:
		cv2.drawContours(image_external, contours, i,255, -1)

#Prepare the internal contour binary mask:
image_internal = np.zeros(image.shape, image.dtype)
for i in range(len(contours)):
	if hierarchy[0][i][3] != -1:
		cv2.drawContours(image_internal, contours, i,255, -1)
plt.figure(figsize=(10,3))
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('external')
plt.imshow(image_external, cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title('internal')
plt.imshow(image_internal, cmap='gray')
plt.tight_layout()
plt.show()