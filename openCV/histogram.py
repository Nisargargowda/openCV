import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #GrayScale Histogram

# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

#BGR to histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)