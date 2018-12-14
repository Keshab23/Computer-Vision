import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('hello.jpg')
img2 = cv2.imread('panda.jpg')

add = img1+img2

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()