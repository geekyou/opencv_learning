import cv2

import numpy as np

image = cv2.imread("face.png")

cv2.imshow("lena",image)
cv2.waitKey(0)

detector =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
rects = detector.detectMultiScale(image , 1.3, 5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
for (x, y, w, h) in rects:
    cv2.rectangle(image,(x, y), (x + w, y + h), (0, 255, 0), 2)
# 将图像显示在屏幕上，

cv2.imshow("Faces", image)
# 等待键盘输出
cv2.waitKey(0)





