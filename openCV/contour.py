import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#First way to blur the image

# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blurred Image', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Image',canny)


#Second way to blur the images using threshold function- looks at an image and binarises that image

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

#common to both ways
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

#To draw the derived contours on the blank image

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contoured Image', blank)

cv.waitKey(0)