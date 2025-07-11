import cv2 as cv
import numpy as np

# VARIABLES

#True while MOUSE BTTN DOWN, False while MOUSE BTTN UP
drawing = False
ix = -1
iy = -1


# FUNCTION
def draw_rectangle(event,x,y,flags,params):
    global ix,iy,drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.rectangle(img, (ix,iy), (x,y), (0,0,255), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix,iy), (x,y), (0,0,255), -1)



# SHOWING THE IMAGE
img = np.zeros((512,512,3))

cv.namedWindow(winname='drawing')
cv.setMouseCallback('drawing',draw_rectangle)


while True:

    cv.imshow('drawing', img)

    if cv.waitKey(1) & 0XFF == 27:
        break

cv.destroyAllWindows()