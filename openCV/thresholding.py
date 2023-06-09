import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding - manually assign the threshold value

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded Image', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Image Inverse', thresh_inv)


# Adaptive Thresholding - inherent threshold value is generated by the system

adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_threshold)

cv.waitKey(0)