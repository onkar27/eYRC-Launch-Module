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
*  Filename: task2_main.py
*  Version: 1.0.0
*  Date: November 28, 2016
*  How to run this file: python task2_main.py
*  Author: e-Yantra Project, Department of Computer Science and Engineering, Indian Institute of Technology Bombay.
* ---------------------------------------------------

* ====================== GENERAL Instruction =======================
* 1. Check for "DO NOT EDIT" tags - make sure you do not change function name of main().
* 2. Return should be a list named occupied_grids and a dictionary named planned_path.
* 3. Do not keep uncessary print statement, imshow() functions in final submission that you submit
* 4. Do not change the file name
* 5. Your Program will be tested through code test suite designed and graded based on number of test cases passed
**************************************************************************
'''

'''
* Team Id :         <Team Id>
* Author List :     Onkar Jagannath Sathe
* Filename:         task2_main.py
* Theme:            Launch Module -- Specific to eYRC
* Functions:        getcolor,getmin,getobj,getoccupied,heu,build,astar,makedic,travel
* Global Variables: RED_MIN,RED_MAX,BLACK_MIN,BLACK_MAX,BLUE_MIN,BLUE_MAX,GREEN_MAX,GREEN_MIN,YELLOW_MIN,YELLOW_MAX,BACK_MIN,BACK_MAX
'''

import numpy as np
import cv2
from heapq import *


'''
* Function Name: getcolor
* Input        : numpy_array_imagepixel(i.e. (B,G,R),RGB_values)
* Output       : color of numpy_array_pixel
* Logic        : Ranges of color's are used and compare as format of (B,G,R)
* Example Call : getcolor(img[i][j])
'''
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

RED_MIN =     np.array([ 0 ,  0,200], np.uint8)
RED_MAX =     np.array([ 50, 50,255], np.uint8)

BLUE_MIN  =   np.array([200,  0,  0], np.uint8)
BLUE_MAX  =   np.array([255, 50, 50],np.uint8)

GREEN_MIN  =  np.array([0  ,200,  0], np.uint8)
GREEN_MAX  =  np.array([50 ,255, 50], np.uint8)

YELLOW_MIN  = np.array([  0,225,225], np.uint8)
YELLOW_MAX  = np.array([ 25,255,255], np.uint8)

BLACK_MIN = np.array([  0,0,0], np.uint8)
BLACK_MAX = np.array([  25,25,25], np.uint8)

BACK_MIN = 0
BACK_MAX = 0

'''
* Function Name: getmin
* Input        : color of pixel (as string)
* Output       : minimum and maximum ranges
* Logic        : Global variables are used for Ranges of color's are used and compare as format of (B,G,R)
* Example Call : getmin('red')
'''
def getmin(color):
    if(color == 'blue'):
        return BLUE_MIN , BLUE_MAX
    elif(color == 'red'):
        return RED_MIN , RED_MAX
    elif(color == 'green'):
        return GREEN_MIN , GREEN_MAX
    elif(color == 'yellow'):
        return YELLOW_MIN , YELLOW_MAX
    elif(color == 'BLACK'):
        return BLACK_MIN,BLACK_MAX
    return BACK_MIN , BACK_MAX


'''
* Function Name: getobj
* Input        : path of image
* Output       : objects in images(as list of tuple[(x,y) coordinates,color,shape,object_total_pixel])
* Logic        : contours are used to find shape using approxPolyDP method,
                 getcolor is for color,
                 inRange and countNonZero for object_total_pixel

* Example Call : getobj('test_images1.jpg')
'''
def getobj(path):
    img = cv2.imread(path)
    #img = cv2.bilateralFilter(img,9,75,75)

    gray = cv2.imread(path,0)
    obj = []
    obj_pix = []
    objects = ['circle','','','triangle','4-sided']
    j=0
    l=1
    while(j<gray.shape[0]):
        i=0
        while(i<gray.shape[1]):
            if(getcolor(img[i+30][j+30])=="WHITE"):
                obj.append(((j/60+1,i/60+1),None,None,None))
                i+=60
                continue
            img_1= gray [i+1:i+60-1,j+1:j+60-1]
            ret , thresh = cv2.threshold(img_1,200,255,1)
            contours , h = cv2.findContours(thresh,1,2)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

            color = getcolor(img[i+30][j+30])
            img_1 = img[i:i+60,j:j+60]
            MIN , MAX = getmin(color)
            if(MIN is not BACK_MIN and MAX is not BACK_MAX):
                obj_pix=cv2.countNonZero(cv2.inRange(img_1, MIN, MAX))
            else:
                obj_pix=0

            if(color!= "BACK" and color != "WHITE"):
                if(len(approx)>10):
                    obj.append(((j/60+1,i/60+1),color,objects[0],obj_pix))
                else:
                    obj.append(((j/60+1,i/60+1),color,objects[len(approx)],obj_pix))
                #print(approx)
            else:
                obj.append(((j/60+1,i/60+1),None,None,obj_pix))
            i+=60
        j+=60
    return obj

'''
* Function Name: getoccupied
* Input        : board object list of tuple[(x,y) coordinates,color,shape,object_total_pixel]
* Output       : Non empty grids as 1st Output
* Logic        : color and shape are None in above list of board they are seperated
* Example Call : getoccupied(board_objects)
'''

def getoccupied(board):
    grids = []
    for i in board :
        #print(i)
        if(i[2]==None):
            continue
        else:
            grids.append(i[0])
    return grids

'''
* Function Name: build
* Input        : board object list , grid (NON Empty Grid list),numpyarray of 10 X 10 size
* Output       : Objects Match_list as dictionary and sorted keys of Match_list as list
* Logic        :
                 build numpy array for algorithm
                 size is checked using object's pixel in board's object
                 shape is compared
                 color is compared
                 if (color is Not None)
                     numpyarray is set to 1
* Example Call : build(board_objects,grid,numpy_array)
'''

def build(board,grid,nmap):
    match_list = {}

    for x in grid:
        i=board[((x[0]-1)*10+x[1])-1]
        nmap[i[0][1]][i[0][0]]=1
        if(i[1]!='BLACK'):
            match = []
            for y in grid :
                j = board[((y[0]-1)*10+y[1])-1]
                if(j[1]!='BLACK' and i[0]!=j[0] and i[1]==j[1] and i[2]==j[2] and abs(i[3]-j[3])<100):
                    match.append(j[0])
            match_list[i[0]]=match
    sortr = match_list.keys()
    sortr.sort()


    return match_list , sortr
'''
* Function Name: heu
* Input        : two coordinates
* Output       : heusterics distance of two points
* Logic        : No. of cells between two points are count
* Example Call : heu((x1,y1),(x2,y2))
'''

def heu(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))


'''
* Function Name: astar
* Input        : numpy_array,start_tuple,goal_tuple
* Output       : dictionary as required
* Logic        : A * algorithm is used
* Example Call : astar(array,start,goal)
'''

def astar(array, start, goal):
    print()
    print(start,goal)

    #all neighbors
    neighbors = [(0,1),(1,0),(-1,0),(0,-1)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heu(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    print((fscore[start], start),"Pushed")
    while oheap:
        print(oheap)
        current = heappop(oheap)[1]
        print(current,"Popped")
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            new_g_score = gscore[current] + heu(current, neighbor)
            if 0 < neighbor[0] < array.shape[0]:
                if 0 < neighbor[1] < array.shape[1]:
                    if array[neighbor[1]][neighbor[0]] == 1:
                        # obstacle identified
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and new_g_score >= gscore.get(neighbor, 0):
                continue

            if  new_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = new_g_score
                fscore[neighbor] = new_g_score + heu(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                print((fscore[neighbor], neighbor),"Pushed")
          #  if there is no path
    return False

'''
* Function Name: makedir
* Input        : list
* Output       : modified list
* Logic        : appropriate list is ordered
* Example Call : makedic(list)
'''
def makedic(temp):
    a=temp[0]
    temp.remove(a)
    value = []
    value.append(a)
    temp.reverse()
    value.append(temp)
    value.append(len(temp)+1)
    #print(value)
    return value

'''
* Function Name: travel
* Input        : path of images
* Output       : occupied grid , dictionary of all paths as Key = tuple(start)
* Logic        : For each objects A* algo is called and minimum path is choosen
                 if No path
                     NO MATCH , empty list , 0 is set
* Example Call : board , paths = travel(image_filename)
'''
def travel(path):
    paths = {}#OrderedDict()
    board = getobj(path)


    nmap = np.array([
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0]])

    grids = getoccupied(board)
    #print(grids)
    match_list ,sortr = build(board,grids,nmap)
    #print(match_list)
    for i in sortr:
        #print(i,match_list[i])
        m_list = match_list[i]
        if(len(m_list)==0):
            paths[tuple(i)]=['NO MATCH','empty list',0]
            continue
        if(len(m_list)!=0):
            all_list = []
            mini = 1000
            is_path = False
            for j in m_list:
                tmp_1=nmap[j[1]][j[0]]
                tmp_2=nmap[i[1]][i[0]]
                nmap[j[1]][j[0]]=nmap[i[1]][i[0]]=0

                temp=astar(nmap,i,j)
                nmap[j[1]][j[0]]=tmp_1
                nmap[i[1]][i[0]]=tmp_2
                if(temp != False and mini>len(temp)):
                    is_path = True
                    all_list=temp
                    mini=len(temp)
                    #print(i,makedic(all_list))
            if(is_path==False):
                paths[tuple(i)]=['NO MATCH','empty list',0]
            else:
                paths[tuple(i)]=makedic(all_list)
    return board , paths


def main(image_filename):

        '''
This function is the main program which takes image of test_images as argument.
Team is expected to insert their part of code as required to solve the given
task (function calls etc).

***DO NOT EDIT THE FUNCTION NAME. Leave it as main****
Function name: main()

******DO NOT EDIT name of these argument*******
Input argument: image_filename

Return:
1 - List of tuples which is the coordinates for occupied grid. See Task2_Description for detail.
2 - Dictionary with information of path. See Task2_Description for detail.
        '''
        board , paths = travel(image_filename)
        occupied_grids = getoccupied(board)             # List to store coordinates of occupied grid -- DO NOT CHANGE VARIABLE NAME
        planned_path = paths            # Dictionary to store information regarding path planning       -- DO NOT CHANGE VARIABLE NAME
        print ( board)



        ##### WRITE YOUR CODE HERE - START

        # cv2.imshow("board_filepath - press Esc to close",cv2.imread(board_filepath))                  - For check - remove
        # cv2.imshow("container_filepath - press Esc to close",cv2.imread(container_filepath))


        # #### NO EDIT AFTER THIS

# DO NOT EDIT
# return Expected output, which is a list of tuples. See Task1_Description for detail.
        return occupied_grids, planned_path



'''
Below part of program will run when ever this file (task1_main.py) is run directly from terminal/Idle prompt.

'''
if __name__ == '__main__':

    # change filename to check for other images
    image_filename = "test_images/test_image2.jpg"
    print(main(image_filename))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
