import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

# 1. Averaging - The intensity of the middle pixel is the avregae value of all the surrounding pixels
# Greater the kernel size, greater is the blur

average = cv.blur(img, (7, 7))
cv.imshow('Average', average)

# 2. Gaussian Blur - the intensity of the middle pixel is the average of the weights of the surrounding pixels
# More natural than the average blur

gausian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gausian)

# 3. Median Blur - finds the median of all the surrounding pixels
# more effective in reducing noise than the other 2

median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# 4. Bilateral Blurring - blurs the image but retains the edges

bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)