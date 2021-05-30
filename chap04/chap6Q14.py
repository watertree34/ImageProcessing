import numpy as np
import cv2

img = cv2.imread('src/norway.jpg')

hsvRgb_mat = np.zeros((180, 256, 3), dtype=np.uint8)

h, s = np.indices(hsvRgb_mat.shape[:2])
hsvRgb_mat[:,:,0] = h
hsvRgb_mat[:,:,1] = s
hsvRgb_mat[:,:,2] = 255
hsvRgb_map = cv2.cvtColor(hsvRgb_mat, cv2.COLOR_HSV2BGR)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
hist = np.clip(hist * 0.005 * 10, 0, 1)


result = hsvRgb_map * hist[:, :, np.newaxis]

cv2.imshow('img', img)
cv2.imshow('hist', np.uint8(result))

cv2.waitKey(0)