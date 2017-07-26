import numpy as np
import cv2
import argparse

def translate(image,x,y):
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
    return shifted

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = "Path to she image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("original",image)

shifted = translate(image,0,100)
cv2.imshow("Shifted down",shifted)

shifted = translate(image,0,-100)
cv2.imshow("Shifted up",shifted)

shifted = translate(image,50,0)
cv2.imshow("Shifted right",shifted)

shifted = translate(image,-50,0)
cv2.imshow("Shifted left",shifted)

cv2.waitKey(0)
