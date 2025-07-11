import cv2 as cv
import numpy as np

def draw_circle(event, x,y,flags, param):
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 32, (0,0,255), 2)
        

cv.namedWindow(winname='img')
cv.setMouseCallback('img',draw_circle)


path = 'DATA/dog_backpack.jpg'
img = cv.imread(path)

if img is None:
    print("Error: The image could not be loaded.")
    exit()


w_ratio = 0.5
h_ratio = 0.5 

img = cv.resize(img, (0,0), img,w_ratio,h_ratio)


while True:

    cv.imshow('img', img)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()