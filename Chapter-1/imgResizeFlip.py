import cv2
img = cv2.imread('nature.jpg')
print('original image shape:', img.shape)
width, height = 256,128
resized_img = cv2.resize(img, (width, height))
print('resized to 128x256 image shape:', resized_img.shape)
img_flip_along_y = cv2.flip(img, 1)
cv2.imshow('Origional Image',img)
cv2.imshow('ResizedImage',resized_img)
cv2.imshow('Flipped Image',img_flip_along_y)
cv2.waitKey(0)