#to read an image
# import cv2 as cv

# img = cv.imread('photos/cat_large.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)








#to read a video

# import cv2 as cv

# capture = cv.VideoCapture('videos/dog.mp4')

# if(capture.isOpened()== False):
#     print('Error opening video file')

# while(capture.isOpened()):
#     ret, frame = capture.read()

#     cv.imshow('Video', frame)

#     if cv.waitKey(25) & 0xFF == ord('q'):
#         break



#to open webcam

import cv2 as cv
capture = cv.VideoCapture(0)
if(capture.isOpened()==False):
    print('Error opening video file')
while(capture.isOpened()):
    ret, frame = capture.read()
    cv.imshow('WebCam', frame)
    cv.waitKey(0)

