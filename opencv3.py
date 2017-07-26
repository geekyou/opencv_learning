import cv2
import argparse


ap = argparse.ArgumentParser ()

ap.add_argument("-i", "--image", required=True, help="Path to the image")

args = vars(ap.parse_args())



image = cv2.imread(args["image"])
cv2.imshow("Original", image) # 计算图像的中心点
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2) # 将图像平均分成四部分并显示
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Left Corner", tl)
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
cv2.waitKey(0)

