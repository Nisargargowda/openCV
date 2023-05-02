import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 1. Laplacan method

lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# 2. Sobel

sobelx = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobely = cv.Sobel(gray, cv.CV_64F, 1, 0)

cv.imshow('Sobel X', sobelx)
cv.imshow('sobel Y', sobely)

merged = cv.bitwise_or(sobelx, sobely)
cv.imshow('Merged', merged)


canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)