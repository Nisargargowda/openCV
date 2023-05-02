import cv2 as cv
#normal img
img = cv.imread('photos/cat.jpg')
#Gray Scale Img
imgGray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#Blured Img
imgBlur = cv.GaussianBlur(img, (9, 9), 0)
#Edge Detector
imgEdge = cv.Canny(img, 100, 100)
#Image Dialation
imgDialate = cv.dilate(imgEdge, (7, 7), iterations=5)
#Image Erosion is opposite to image dilation
imgErosion = cv.erode(imgDialate, (7, 7), iterations=5)
#Image Reesize
imgResize = cv.resize(img, (500, 500))
#image crop
imgCrop = img[0:200, 200:500]


cv.imshow('Cat', img)
cv.imshow('GrayScale', imgGray)
cv.imshow('Blured Image', imgBlur)
cv.imshow('Canny Img', imgEdge)
cv.imshow('Dilated img', imgDialate)
cv.imshow('Eroded Image', imgErosion)
cv.imshow('Resized img0', imgResize)
cv.imshow('Croppped image', imgCrop)
cv.waitKey(0)