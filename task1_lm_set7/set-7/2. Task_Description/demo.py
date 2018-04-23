import numpy as np
import cv2
img = cv2.imread('test_images/board_7.jpg',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img,5)
a,img = cv2.threshold(img,0,255,0)
img = cv2.Canny(img,0,255)
contour ,img = cv2.findContours(img,2,1)
print(img)
