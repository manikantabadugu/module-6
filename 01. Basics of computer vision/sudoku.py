import cv2
import numpy as np
image= cv2.imread('sudoku.png')
def rescaleFrame(frame, scale=0.75):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions= (width,height)
    return cv2.resize(frame, dimensions, interpolation= cv2.INTER_AREA)
img_res= rescaleFrame(image,0.3)
img_res= cv2.cvtColor(img_res, cv2.COLOR_BGR2GRAY)

copy= img_res.copy()

img_blur = cv2.GaussianBlur(copy, (3,3),0)
#thresholding
img_thresh=cv2.adaptiveThreshold(img_blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

img_bit = cv2.bitwise_not(img_thresh, img_thresh)

kernel = np.ones((3,3), np.uint8)
img_dilate = cv2.dilate(img_bit, kernel)



cv2.imshow('image', img_dilate)
cv2.waitKey()
