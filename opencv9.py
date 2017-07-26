import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Cat",image)

rectangle = np.ones(image.shape[:2],dtype='uint8')
cv2.rectangle(rectangle,(380,100),(575,200),255,-1)
cv2.imshow("Rectangle",rectangle)

circle = np.ones(image.shape[:2],dtype='uint8')
cv2.circle(circle,(475,180),105,0,-1)
cv2.imshow("Circle",circle)

bitwisexor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("Birwisexor",bitwisexor)

mask = bitwisexor
cv2.imshow("Mask",mask)
masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey(0)

