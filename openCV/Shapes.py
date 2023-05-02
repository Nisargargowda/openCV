import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)
# blank[0:150] = 0, 255, 0
# cv.imshow('Green', blank)

# #Drawing a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=-1)
# cv.imshow('Rectangle', blank)
# cv.waitKey(0)

# #Drawing a circle
# new_blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.circle(new_blank, (250, 250), 40, (255, 0, 0), thickness=3)
# cv.imshow('Circle', new_blank)
# cv.waitKey(0)

# #draw a line
# cv.line(new_blank, (0, 0), (500, 500), (255, 255, 255), thickness=3)
# cv.imshow('Line', new_blank)
# cv.waitKey(0)

#how to write text on an image
cv.putText(blank, 'Helloo', (250, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)