import numpy as np
import cv2
import math

def mod(x):
    if(x<0):
        x*=-1
    return x

def getdist(x1,y1,x2,y2):
    return pow(mod(x2-x1)*mod(x2-x1)+mod(y2-y1)*mod(y2-y1),0.5)

def getcolor(a):
    x=a[0]
    y=a[1]
    z=a[2]
    if(x<15 and y<15 and z<15):
        return "BLACK"
    elif(x>225 and y<15 and z<15):
        return "BLUE"
    elif(x<15 and y<15 and z>225):
        return "RED"
    elif(x<15 and y>225 and z<15):
        return "GREEN"
    elif(x>225 and y>225 and z>225):
        return "WHITE"
    elif(x<15 and y>225 and z>225):
        return "YELLOW"
    return "BACK"

def getshape(image,x,y):
    list = [[0,0],[0,0],[0,0],[0,0]]
    
    i=x
    j=y
    temp=getcolor(image[x][y])
    while(1):
        i-=1
        if(temp!=getcolor(image[i][y])):
            break
    list[0][0]=getdist(i,j,x,y)
    i=x
    j=y
    while(1):
        j-=1
        if(temp!=getcolor(image[x][j])):
            break
    list[1][0]=getdist(i,j,x,y)
    i=x
    j=y
    while(1):
        j-=1
        i-=1
        if(temp!=getcolor(image[i][j])):
            break
    list[2][0]=getdist(i,j,x,y)
    i=x
    j=y
    temp=getcolor(image[x][y])
    while(1):
        i+=1
        if(temp!=getcolor(image[i][y])):
            break
    list[0][1]=getdist(i,j,x,y)
    i=x
    j=y
    while(1):
        j+=1
        if(temp!=getcolor(image[x][j])):
            break
    list[1][1]=getdist(i,j,x,y)
    i=x
    j=y
    while(1):
        j+=1
        i+=1
        if(temp!=getcolor(image[i][j])):
            break
    list[2][1]=getdist(i,j,x,y)
    i=x
    j=y
    while(1):
        j-=1
        i+=1
        if(temp!=getcolor(image[i][j])):
            break
    list[3][0]=getdist(i,j,x,y)
    i=x
    j=y
    while(1):
        j+=1
        i-=1
        if(temp!=getcolor(image[i][j])):
            break
    list[3][1]=getdist(i,j,x,y)
    return list
    
def main():    
    img = cv2.imread('new.jpg',1)
    print(1,getcolor(img[50][50]),img[50][50])
    print(2,getcolor(img[50][150]),img[50][150])
    print(3,getcolor(img[50][250]),img[50][250])
    print(4,getcolor(img[50][350]),img[50][350])
    print(5,getcolor(img[150][50]),img[150][50])
    print(6,getcolor(img[150][150]),img[150][150])
    print(7,getcolor(img[150][250]),img[150][250])
    print(8,getcolor(img[150][350]),img[150][350])
    print(9,getcolor(img[250][50]),img[250][50])
    print(10,getcolor(img[250][150]),img[250][150])
    print(11,getcolor(img[250][250]),img[250][250])
    print(12,getcolor(img[250][350]),img[250][350])
    print(13,getcolor(img[350][50]),img[350][50])
    print(14,getcolor(img[350][150]),img[350][150])
    print(15,getcolor(img[350][250]),img[350][250])
    print(16,getcolor(img[350][350]),img[350][350])
    print(getshape(img,50,150))    
    return

main()
