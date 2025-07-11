import cv2 as cv
import numpy as np


def draw_circle(event, x,y,flags, param):
    
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 20, (0,255,0), -1)

    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 20, (0,0,255), -1)
        

cv.namedWindow(winname='Draw_img')

cv.setMouseCallback('Draw_img',draw_circle)




##############################################
################   SHOWING  ##################
##############################################


img = np.zeros((512,512,3))

while True:

    cv.imshow('Draw_img', img)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()