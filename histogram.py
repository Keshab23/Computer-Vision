import cv2
import numpy as np
import matplotlib.pyplot as plt

#Load an image and display it:
grey = cv2.imread('nature.jpg', 0)
cv2.imshow('original grey', grey)
cv2.waitKey()
cv2.destroyAllWindows()

#Compute a histogram function:
hist, bins = np.histogram(grey, 256, [0, 255])

#Plot histogram and display it:
plt.fill(hist)
plt.xlabel('pixel value')
plt.show()