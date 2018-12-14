import cv2
img = cv2.imread("hello.jpg")
cv2.imwrite("helloCopy.png",img)
#cv2.waitKey(0)