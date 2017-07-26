import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap .add_argument('-i','--image',required = True,help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original",image)

(B,G,R) = cv2.split(image)

zeros = np.zeros(image.shape[:2],dtype="uint8")

cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Rad",cv2.merge([zeros,zeros,R]))



cv2.waitKey(0)