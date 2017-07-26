import numpy as np
import cv2

canvas = np.zeros((400,600,3),dtype="uint8")

green = (0,255,0)

cv2.line(canvas,(0,0),(600,400),green)

cv2.imshow("canvas",canvas)

cv2.waitKey(0)

red = (0,0,255)

blue = (255,0,0)

cv2.line(canvas,(600,0),(0,400),red,3)

cv2.imshow("canvas",canvas)

cv2.waitKey(0)

cv2.rectangle(canvas,(100,100),(150,150),green,2)

cv2.imshow("canvas",canvas)

cv2.waitKey(0)


cv2.rectangle(canvas,(300,50),(325,125),blue,-1)

cv2.imshow("canvas",canvas)

cv2.waitKey(0)

white = (255,255,255)

cv2.circle(canvas,(300,300),50,white)

cv2.imshow("canvas",canvas)

cv2.waitKey(0)

color = (255,0,255)

cv2.circle(canvas,(500,200),40,color,-1)

cv2.imshow("canvas",canvas)

cv2.waitKey(0)