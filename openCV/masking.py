import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank img', blank)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

wierd_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("weird shape", wierd_shape)

masked = cv.bitwise_and(img, img, mask=wierd_shape)
cv.imshow('Masked Image', masked)

cv.waitKey(0)