#旋转

import cv2
import numpy as np
import argparse

def rotate(image,angle,center = None,scale = 1.0):
    #获取图片尺寸
    (h,w) = image.shape[:2]
    if center == None:
        center = (w//2,h//2)

    M = cv2.getRotationMatrix2D(center,angle,scale)
    rotated = cv2.warpAffine(image,M,(w,h))

    return rotated

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

cv2.imshow("Original",image)

rotated = rotate(image,45)
cv2.imshow("Rotated by 45 Degrees",rotated)

rotated = rotate(image,-45)
cv2.imshow("Rotated by -45 Degrees",rotated)

rotated = rotate(image,90)
cv2.imshow("Rotated by 90 Degrees",rotated)

rotated = rotate(image,-90)
cv2.imshow("Rotated by -90 Degrees",rotated)

rotated = rotate(image,180)
cv2.imshow("Rotated by 180 Degrees",rotated)

cv2.waitKey(0)


