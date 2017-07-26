#识别条形码


import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = "Path to image")
args = vars(ap.parse_args())


image = cv2.imread(args['image'])
cv2.imshow("Original",image)

#变为灰度
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey",gray)


#转化为高水平梯度和低竖直梯度
gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)

# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

cv2.imshow("Gradient",gradient)

#去噪&二值化

blurred = cv2.blur(gradient, (9, 9))  #平均模糊
(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

cv2.imshow("Blurred",blurred)

cv2.imshow("Thresh",thresh)


#矩形内核

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Kernel",kernel)
cv2.imshow("Closed",closed)

#进行腐蚀和膨胀

closed = cv2.erode(closed, None, iterations = 4)
closed = cv2.dilate(closed, None, iterations = 4)

cv2.imshow("Closed",closed)



#找到轮廓

# find the contours in the thresholded image, then sort the contours
# by their area, keeping only the largest one
(_,cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))

# draw a bounding box arounded the detected barcode and display the
# image
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image",image)


cv2.waitKey(0)


