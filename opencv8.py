# Get cat

import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

cv2.imshow("Cat",image)

rectangle = np.ones(image.shape[0:2],dtype="uint8")
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("Rectangle",rectangle)

circle = np.ones(image.shape[0:2],dtype="uint8")
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("Circle",circle)

bitwiseand = cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND",bitwiseand)

bitwiseor = cv2.bitwise_or(rectangle,circle)
cv2.imshow("OR",bitwiseor)

bitwisenot = cv2.bitwise_not(circle)
cv2.imshow("NOT",bitwisenot)

bitwisexor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("XOR",bitwisexor)

cv2.waitKey(0)



