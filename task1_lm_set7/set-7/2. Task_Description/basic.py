'''import numpy as np
import cv2
import math
def getdist(x1,y1,x2,y2):
    return pow(mod(x2-x1)*mod(x2-x1)+mod(y2-y1)*mod(y2-y1),0.5)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

def getcolor(a):
    x=a[0]
    y=a[1]
    z=a[2]
    if(x<50 and y<50 and z<50):
        return "BLACK"
    elif(x>200 and y<50 and z<50):
        return "blue"
    elif(x<50 and y<50 and z>200):
        return "red"
    elif(x<50 and y>200 and z<50):
        return "green"
    elif(x>200 and y>200 and z>200):
        return "WHITE"
    elif(x<25 and y>225 and z>225):
        return "yellow"
    return "BACK"
import cv2
import numpy as np

RED_MIN =     np.uint8([[[0,0,200 ]]])
RED_MIN = cv2.cvtColor(RED_MIN,cv2.COLOR_BGR2HSV)

RED_MAX =     np.uint8([[[50,50,255 ]]])
RED_MAX = cv2.cvtColor(RED_MAX,cv2.COLOR_BGR2HSV)

BLUE_MIN  =    np.uint8([[[200,0,0 ]]])
BLUE_MIN = cv2.cvtColor(BLUE_MIN,cv2.COLOR_BGR2HSV)

BLUE_MAX  =    np.uint8([[[255,50,50 ]]])
BLUE_MAX = cv2.cvtColor(BLUE_MAX,cv2.COLOR_BGR2HSV)

GREEN_MIN  =   np.uint8([[[0,200,0 ]]])
GREEN_MIN = cv2.cvtColor(GREEN_MIN,cv2.COLOR_BGR2HSV)

GREEN_MAX  =   np.uint8([[[50,255,50 ]]])
GREEN_MAX = cv2.cvtColor(GREEN_MAX,cv2.COLOR_BGR2HSV)

YELLOW_MIN  =  np.uint8([[[0,225,225 ]]])
YELLOW_MIN = cv2.cvtColor(YELLOW_MIN,cv2.COLOR_BGR2HSV)

YELLOW_MAX  =  np.uint8([[[25,25,255 ]]])
YELLOW_MAX = cv2.cvtColor(YELLOW_MAX,cv2.COLOR_BGR2HSV)

cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('dave.jpg',0)
img = cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in xrange(4):
plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
plt.title(titles[i])
plt.xticks([]),plt.yticks([])
plt.show()
