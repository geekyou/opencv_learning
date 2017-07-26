#缩放

import cv2
import argparse

def resize(image,width = None,height = None,inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height/float(h)
        dim = (int(w*r),height)
    else:
        r = width/float(w)
        dim = (width,int(h*r))
    resized = cv2.resize(image,dim,interpolation=inter)
    return resized

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])


methods = [
    ("cv2.INTER_NEAREST",cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR",cv2.INTER_LINEAR),
    ("cv2.INTER_AREA",cv2.INTER_AREA),
    ("cv2.INTER_CUBIC",cv2.INTER_CUBIC),
    ("cv2.INTER_IANCZOS4",cv2.INTER_LANCZOS4)]




for (name,method) in methods:
    #放大三倍
    resized = resize(image,width=image.shape[1]*3,inter=method)
    cv2.imshow("Zoom In method: {} ".format(name),resized)

    #缩小两倍
    resized = resize(image,width=image.shape[1]//2,inter=method)
    cv2.imshow("Zoom Out method:{}".format(name),resized)
    cv2.waitKey(0)



