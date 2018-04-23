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
    elif(x<20 and y>225 and z>225):
        return "YELLOW"
    return "BACK"

def list_(image,x,y):
    list = [[0,0],[0,0]]
    
    i=x
    j=y
    if(getcolor(image[x][y])=="BACK"):
        return list
    temp="BLACK"
    
    #up
    while(1):
        i-=1
        if(temp==getcolor(image[i][y])or getcolor(image[i][y])== "BACK"):
            break
    list[0][0]=x-i
    
    #left
    i=x
    j=y
    while(1):
        j-=1
        if(temp==getcolor(image[x][j])or getcolor(image[x][j])== "BACK"):
            break
    list[1][0]=y-j
    
    #down
    i=x
    j=y
    while(1):
        i+=1
        if(temp==getcolor(image[i][y]) or getcolor(image[i][y])== "BACK"):
            break
    list[0][1]=i-x
    
    #right
    i=x
    j=y
    while(1):
        j+=1
        if(temp==getcolor(image[x][j]) or getcolor(image[x][j])== "BACK"):
            break
    list[1][1]=j-y
    
    #print(list)
    return list

def ie(x,y):
    if(mod(x-y)>2):
        return 0
    else:
        return 1

def getshape(image,x,y):
    if(getcolor(image[x][y])=="BACK"):
        return "EMP"
    list = list_(image,x,y)
    #print(list)
    if(ie(list[0][0],list[0][1]) and ie(list[1][0],list[1][1])): 
        if(ie(list[0][0],list[1][0]) and ie(list[0][1],list[1][1])):
            if(getcolor(image[x-list[0][0]-2][y-list[0][1]-2])=="BACK"):
                return "CIR"
            else:
                return "SQR"
        else:
            return "REC"
    else:
        return "TRI"
   
def main():
    img = cv2.imread('container_5.jpg',1)
   
    print(1,getshape(img,50,50))
    print(2,getshape(img,50,150))
    print(3,getshape(img,50,250))    
    print(4,getshape(img,50,350))
    print()
    print(5,getshape(img,150,50))    
    print(6,getshape(img,150,150))
    print(7,getshape(img,150,250))    
    print(8,getshape(img,150,350))
    print()
    print(9,getshape(img,250,50))    
    print(10,getshape(img,250,150))
    print(11,getshape(img,250,250))    
    print(12,getshape(img,250,350))
    print()
    print(13,getshape(img,350,50))    
    print(14,getshape(img,350,150))
    print(15,getshape(img,350,250))    
    print(16,getshape(img,350,350))
    return

main()
