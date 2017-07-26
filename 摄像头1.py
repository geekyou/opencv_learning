#捕获单张照片

import cv2
import numpy as np
import time

cv2.namedWindow("test")


cap = cv2.VideoCapture(0)

while True:

    (success,image) = cap.read()

# print(success)
    cv2.imshow("Camera",image)


    detector =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    rects = detector.detectMultiScale(image , 1.3, 5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in rects:
        cv2.rectangle(image,(x, y), (x + w, y + h), (0, 255, 0), 2)
# 将图像显示在屏幕上，

    cv2.imshow("Faces", image)
    keycode = cv2.waitKey(1)
    if chr(keycode) == 'q':
        break
    time.sleep(0.1)

# 等待键盘输出

# cv2.waitKey(0)
#
