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
        return "blue"
    elif(x<15 and y<15 and z>225):
        return "red"
    elif(x<15 and y>225 and z<15):
        return "green"
    elif(x>225 and y>225 and z>225):
        return "WHITE"
    elif(x<20 and y>225 and z>225):
        return "yellow"
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
        if(temp==getcolor(image[i][y]) or getcolor(image[i][y])== "BACK"):
            break
    list[0][0]=x-i
    
    #left
    i=x
    j=y
    while(1):
        j-=1
        if(temp==getcolor(image[x][j]) or getcolor(image[x][j])== "BACK"):
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
                return "Circle"
            else:
                return "SQR"
        else:
            return "REC"
    else:
        return "Triangle"
   
def getobj(s):
    img = cv2.imread(s,1)
    i=50
    cnt=1
    objects = []
    
    while(i<=img.shape[0]):
        j=50
        while(j<=img.shape[1]):
            objects.append(tuple((cnt,getcolor(img[i][j]),getshape(img,i,j))))
            cnt+=1
            j+=100
        i+=100
    return objects

def getmatch():
    board = getobj('board_7.jpg')
    container = getobj('container_4.jpg')
    output = []
    i=0
    while(i<9):
        j=0
        while(j<16):
            if board[i][1] == container[j][1] and board[i][2] == container[j][2]:
                output.append(((board[i][0],container[j][0])))
                break
            j+=1
        if(j==16):
            output.append((i+1,0))
        i+=1
        
    return output
print(getmatch())



