import cv2

import argparse

#image = cv2.imread("flower.jpg")

#print(image)

ap = argparse.ArgumentParser ()

ap.add_argument("-i", "--image", required=True, help="Path to the image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("flower",image)

cv2.waitKey(0)

print("height %d pixels"%(image.shape[0]))
print("width %d pixels"%(image.shape[1]))
print("channels %d "%(image.shape[2]))