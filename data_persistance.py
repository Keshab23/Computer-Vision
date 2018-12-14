import cv2, numpy as np
'''
mat = np.random.rand(100, 100).astype(np.float32)
print('Shape:', mat.shape)
print('Data type:', mat.dtype)
np.savetxt('mat.txt', mat)

'''
mat = np.loadtxt('mat.txt').astype(np.float32)
print('Shape:', mat.shape)
print('Data type:', mat.dtype)