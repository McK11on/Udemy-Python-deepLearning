import cv2 as cv

path = 'DATA/gorilla.jpg'
img = cv.imread(path)

if img is None:
    print("Error: The image could not be loaded.")
    exit()


w_ratio = 0.5
h_ratio = 0.5 


resize_img = cv.resize(img, (0,0), img,w_ratio,h_ratio)

while True:

    cv.imshow('gorilla', resize_img)
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()