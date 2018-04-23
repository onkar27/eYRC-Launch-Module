import cv2
import numpy as np
MIN  = np.array([254,254,254], np.uint8)
MAX  = np.array([255,255,255], np.uint8)
filename = 'container_1.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[255,255,255]

def getobjpixel(img):
    obj_pix =[]
    i=0
    l=1
    while(i<img.shape[0]):
        j=0
        while(j<img.shape[1]):
            img_1= img [i:i+100,j:j+100]
            obj_pix.append(tuple((l,cv2.countNonZero(cv2.inRange(img_1, MIN, MAX))-64)))
            l+=1
            j+=100
        i+=100

    return obj_pix
print(getobjpixel(img))
