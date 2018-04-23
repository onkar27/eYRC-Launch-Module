# -*- coding: utf-8 -*-
'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*  
*  Author: e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
* ---------------------------------------------------
*  Theme: Launch a Module
*  Filename: task1_main.py
*  Version: 1.0.0  
*  Date: November 11, 2016
*  How to run this file: python task1_main.py
*  Author: e-Yantra Project, Department of Computer Science and Engineering, Indian Institute of Technology Bombay.
* ---------------------------------------------------

* ====================== GENERAL Instruction =======================
* 1. Check for "DO NOT EDIT" tags - make sure you do not change function name of main().
* 2. Return should be board_objects and output_list. Both should be list of tuple 
* 3. Do not keep uncessary print statement, imshow() functions in final submission that you submit
* 4. Do not change the file name
* 5. Your Program will be tested through code test suite designed and graded based on number of test cases passed 
**************************************************************************
'''
import numpy as np
import cv2
import math

def mod(x):
    if(x<0):
        x*=-1
    return x

def getdist(x1,y1,x2,y2):
    return pow(mod(x2-x1)*mod(x2-x1)+mod(y2-y1)*mod(y2-y1),0.5)

RED_MIN =     np.array([ 0 ,  0,200], np.uint8)
RED_MAX =     np.array([ 50, 50,255], np.uint8)

BLUE_MIN  =   np.array([200,  0,  0], np.uint8)
BLUE_MAX  =   np.array([255, 50, 50],np.uint8)

GREEN_MIN  =  np.array([0  ,200,  0], np.uint8)
GREEN_MAX  =  np.array([50 ,255, 50], np.uint8)

YELLOW_MIN  = np.array([  0,225,225], np.uint8)
YELLOW_MAX  = np.array([ 25,255,255], np.uint8)

BACK_MIN = 0
BACK_MAX = 0

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
                return "4-sided"
        else:
            return "4-sided"
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


def getmin(color):
    if(color == 'blue'):
        return BLUE_MIN , BLUE_MAX
    elif(color == 'red'):
        return RED_MIN , RED_MAX
    elif(color == 'green'):
        return GREEN_MIN , GREEN_MAX
    elif(color == 'yellow'):
        return YELLOW_MIN , YELLOW_MAX
    return BACK_MIN , BACK_MAX

def getobjpixel(img):
    obj_pix =[]
    i=0
    l=1
    while(i<img.shape[0]):
        j=0
        while(j<img.shape[1]):
            img_1= img [i:i+100,j:j+100]
            MIN , MAX = getmin(getcolor(img_1[50][50]))
            if(MIN is not BACK_MIN and MAX is not BACK_MAX):
                obj_pix.append(tuple((l,cv2.countNonZero(cv2.inRange(img_1, MIN, MAX)))))
            else:
                obj_pix.append(tuple((l,0)))
            l+=1
            j+=100
        i+=100

    return obj_pix


def getmatch(board,path,board_p):
    container = getobj(path)
    cont_p  = getobjpixel(cv2.imread(path))
    output = []
    i=0
    while(i<len(board)):
        j=0
        while(j<len(container)):
            if board[i][1] == container[j][1] and board[i][2] == container[j][2] :
                 if mod(board_p[i][1]-cont_p[j][1]) < 100  :
                    output.append(tuple(((board[i][0],container[j][0]))))
                    break
            j+=1
        if(j==len(container)):
            output.append(tuple((i+1,0)))
        i+=1
        
    return output


# ******* WRITE YOUR FUNCTION, VARIABLES etc HERE


def main(board_filepath, container_filepath):
	'''
This function is the main program which takes image of game-board and
container as argument. Team is expected to insert their part of code as
required to solve the given task (function calls etc).

***DO NOT EDIT THE FUNCTION NAME. Leave it as main****
Function name: main()

******DO NOT EDIT name of these argument*******
Input argument: board_filepath and container_filepath.

Return: 
1 - List of tuples which is the expected final output. See Task1_Description for detail. 
2 - List of tuples for objects on board. See Task1_Description for detail. 
	''' 

	board_objects = []		# List to store output of board -- DO NOT CHANGE VARIABLE NAME
	output_list = []		# List to store final output 	-- DO NOT CHANGE VARIABLE NAME
	
        board_objects = getobj(board_filepath)		                          # List to store output of board -- DO NOT CHANGE VARIABLE NAME
        output_list   = getmatch(board_objects,container_filepath,getobjpixel(cv2.imread(board_filepath)))            		# List to store final output 	-- DO NOT CHANGE VARIABLE NAME
        print board_objects
        print output_list


	##### WRITE YOUR CODE HERE - STARTS

	# cv2.imshow("board_filepath - press Esc to close",cv2.imread(board_filepath))			- For check - remove
	# cv2.imshow("container_filepath - press Esc to close",cv2.imread(container_filepath))


	# #### NO EDIT AFTER THIS

# DO NOT EDIT
# return Expected output, which is a list of tuples. See Task1_Description for detail.
	return board_objects, output_list	



'''
Below part of program will run when ever this file (task1_main.py) is run directly from terminal/Idle prompt.

'''
if __name__ == '__main__':
    

	board_filepath = "test_images/board_1.jpg"    			# change filename of board provided to you 
	container_filepath = "test_images/container_1.jpg"		# change filename of container as required for testing

	main(board_filepath,container_filepath)

	cv2.waitKey(0)
	cv2.destroyAllWindows()    
