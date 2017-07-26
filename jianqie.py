#剪切

import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original",image)

#mouth = image[85:250,85:200]
#cv2.imshow("mouse1",mouth)

mouth = image[100:450,150:480]
cv2.imshow("Mouse2",mouth)

#mouse = image[85:250,85:220]
#cv2.imshow("Mouse3",mouth)

cv2.waitKey(0)