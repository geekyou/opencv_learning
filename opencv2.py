import cv2

import argparse

ap = argparse.ArgumentParser ()

ap.add_argument("-i", "--image", required=True, help="Path to the image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("original_img",image)

image[0:5,0:5] = (0,255,0)
cv2.imshow("color1",image)

image[0:5,0:5] = (0,0,255)
cv2.imshow("color2",image)

image[0:5,0:5] = (255,0,0)
cv2.imshow("color3",image)

cv2.waitKey(0)