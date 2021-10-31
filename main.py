import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread("shape.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 100, 200)

lines = cv.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 0.9, 80, 110, 39, 50)

for co, i in enumerate(circles[0, :], start=1):
    cv.circle(image, (int(i[0]), int(i[1])), int(i[2]), (0, 255, 0), 10)

for line in lines:
    for x1, y1, x2, y2 in line:
        cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 10)

plt.imshow(image)
plt.show()

# cv.imwrite('shape1.jpg', image)

