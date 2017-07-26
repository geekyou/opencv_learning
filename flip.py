#翻转
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original",image)

#横向翻转
flipped = cv2.flip(image,1)
cv2.imshow("flipped Horizontally",flipped)

#纵向翻转
flipped = cv2.flip(image,0)
cv2.imshow("flipped Vertically",flipped)

#同时反转
flipped = cv2.flip(image,-1)
cv2.imshow("flipped Horizontally & Vertically",flipped)

cv2.waitKey(0)