import argparse
import cv2
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='/home/keshab/Documents/CV_Projects/hello.jpg',
help='Image path.')
params = parser.parse_args()
img = cv2.imread(params.path)
assert img is not None # check if the image was successfully loaded
print('For origional image')
print('read {}'.format(params.path))
print('shape:', img.shape)
print('dtype:', img.dtype)
print('For gray scale image')
cv2.imshow('ImageWindow',img)

img1 = cv2.imread(params.path, cv2.IMREAD_GRAYSCALE)
assert img1 is not None
print('read {} as grayscale'.format(params.path))
print('shape:', img1.shape)
print('dtype:', img1.dtype)
cv2.imshow('ImageWindowNew',img1)
cv2.waitKey(0)

cv2.destroyAllWindows()