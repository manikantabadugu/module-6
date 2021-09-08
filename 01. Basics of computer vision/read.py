# import cv2 as cv
## displaying images and videos
# img=cv2.imread('manikanta.jpg')
# cv2.imshow('flowers',img)
# capture= cv2.VideoCapture('vd.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv2.imshow('video', frame)
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release

# cv2.waitKey()
# cv2.destroyAllWindows()

# cv.imshow('me', img)








##resizing images and videos
# def rescaleFrame(frame, scale=0.75):
#     width= int(frame.shape[1]*scale)
#     height= int(frame.shape[0]*scale)
#     dimensions= (width,height)
#     return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
# cv.waitKey()
# capture= cv.VideoCapture('vd.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)
#     frame_resized= rescaleFrame(frame,0.2)
    
#     cv.imshow('video resized', frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release


# cv.waitKey()
# cv.destroyAllWindows()







##drawing shapes on images

# import numpy as np
# import pandas as pd
# blank=np.zeros((500,500,3), dtype='uint8')
# blank[20:60,50:100]=(0,255,0)

# cv.rectangle(blank,(200,200),(300,300),(0,0,255),thickness=-1)
# cv.rectangle(blank,(200,180),(220,200),(0,0,255),thickness=-1)

# cv.circle(blank,(250,250),20,(255,255,255),thickness=-1)

# cv.line(blank,(0,0),(500,500),(255,255,255), thickness=3)
# cv.line(blank,(0,500),(500,0),(255,255,255), thickness=3)

# cv.putText(blank,'Hello user',(200,200), cv.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255),thickness=1)

# cv.imshow('blank',blank)
# cv.waitKey()





#essential functions
# import cv2 as cv
# img= cv.imread('manikanta.jpeg')
# grey_img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# def rescaleFrame(frame, scale=0.75):
#     width= int(frame.shape[1]*scale)
#     height= int(frame.shape[0]*scale)
#     dimensions= (width,height)
#     return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
# cv.waitKey()
# grey_res= rescaleFrame(grey_img,0.15)

# #blur image
# blur= cv.GaussianBlur(grey_res,(7,7),cv.BORDER_DEFAULT)

# #edge cascade
# canny= cv.Canny(blur, 100,150)

# #dilate image
# dilated=cv.dilate(grey_res,(7,7), iterations=2 )

# #eroding
# eroded = cv.erode(dilated,(3,3), iterations=3)

# #resize
# resize = cv.resize(grey_res,(500,500), interpolation= cv.INTER_LINEAR)

# # 'CROPPED
# cropped = grey_res[20:200,40:400]
# cv.imshow('img', cropped)
# cv.imshow('img', grey_res)
# cv.waitKey()




#countours
# import cv2 as cv
# import numpy as np

# img= cv.imread('manikanta.jpeg')

# gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# def rescaleFrame(frame, scale=0.75):
#     width= int(frame.shape[1]*scale)
#     height= int(frame.shape[0]*scale)
#     dimensions= (width,height)
#     return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
# cv.waitKey()
# grey_res= rescaleFrame(gray,0.15)
# blank = np.zeros(grey_res.shape, dtype='uint8')


# # blur= cv.GaussianBlur(grey_res,(5,5), cv.BORDER_DEFAULT)
# canny = cv.Canny(grey_res, 125,175)
# # contours, heirarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 

# ret, thresh = cv.threshold(grey_res,125,255, cv.THRESH_BINARY)
# contours, heirarchy = cv.findContours(grey_res, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(blank, contours, -1, (255,255,255),1)
# cv.imshow('blank', blank)
# print(len(contours))
# cv.imshow('THRESH',   thresh)
# # cv.imshow('canny edges', canny)

# cv.waitKey(0)


#color spaces

import cv2 as  cv
import numpy as np
img= cv.imread('annotations.jpg')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('image', img)
b,g,r = cv.split(img)
cv.imshow('blue', r)

# actual= cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('original', actual)

cv.waitKey(0)
