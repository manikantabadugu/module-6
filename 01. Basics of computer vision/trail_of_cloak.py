import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(3)
background=0
cv2.imshow(cap)
# for i in range(30):
# 	ret,background = cap.read()
