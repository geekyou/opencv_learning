#图像加减
import numpy as np
import cv2

grey = np.ones((100,100,3),dtype=np.uint8)*100

cv2.imshow("Grey",grey)

# cv2.waitKey(0)

# bar = np.ones((50,1,3),dtype=np.uint8)*0
# for i in np.arange(1,256):
#     col = np.ones((50,1,3),dtype=np.uint8)*i
#     bar = np.concatenate((bar,col),axis=1)
# cv2.imshow("Bar",bar)
# cv2.waitKey(0)

M = np.ones((100,100,3),dtype=np.uint8)*100

grey = grey + M
cv2.imshow("Grey1",grey)

grey = grey + M
cv2.imshow("Grey2",grey)

cv2.waitKey(0)
