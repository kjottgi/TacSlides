import copy
from typing import Union

from PIL import Image
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import math

from warslide import algorithmGUI

#Flush mode warslide generator idea..
refactor_factor = 50
#Have two sides.
x = 5
#img = np.array(Image.open('./row.png'))
#print(type(img))

def color(img: np.ndarray,x:int,y:int,boundary:list[list[int,int]], color: list[int,int,int],direction:str="-") -> Union[list[int,int],None]:
    """Given an image, in ndarray form, and a integer coordinate(x,y),color the direction
    a different color with the color provided, then return all new coordinates.
    Boundary is the boundary of the region, given by a x and y value of the boundary.
    Return if it was successful
    #Note that when doing img[y,x], the first coordinate is the y, then the next is the x.
    """
    new_coordinate = [x,y]
    match direction:
        case "N":
            new_coordinate[0]= new_coordinate[0]-1
        case "S":
            new_coordinate[0]= new_coordinate[0]+1
        case "E":
            new_coordinate[1]= new_coordinate[1]-1
        case "W":
            new_coordinate[1]= new_coordinate[1]+1 #For each direction, find the new coordinate.
        case "-":
            pass #We do nothing with "-"
        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return False #If the direction is not valid, reutrn False

    try:
        if not valueInList(new_coordinate, boundary):
            #IF we are not in the boundary, make that point the color.
            img[new_coordinate[0],new_coordinate[1]] = color
            return [new_coordinate[0],new_coordinate[1]]
        return None #In this case, since we are on the boundary, technically.. it passed
    except (Exception):
        return None #If a error errors(ex not in numpy array return fales)

def samecolor(img: np.ndarray, coord1: list[int,int], coord2: list[int,int]) -> bool:
    """Take two integer coordinates and return if the color are these two values are the same"""
    color_1 = img[coord1[0],coord1[1]]
    color_2= img[coord2[0],coord2[1]]
    equality = color_1==color_2
    for RGB in equality:
        if RGB==False:
            return False
    return True
def valueInList(value: list[int,int], lst: list[list[int,int]])-> bool:
    """Takes a value, and checks if a part of the list has that exact pair"""
    for pair in lst:
        if pair[0]==value[0] and pair[1]==value[1]:
            return True
    return False
def isPointDone(img: np.ndarray, coord1: list[int,int], boundary: list[list[int,int]],starting: list[list[int,int]])-> bool:
    """Takes a image, a point, and a boundary. This checks if all the surrounding area on top, and on the side
    of the point is either a boundary or the same color.
    Coord is in the form [y,x]
    Starting is also in the form [y,x]
    All the boundary coordinates are in the form [y,x]

    """
    north_coord = [coord1[0]-1,coord1[1]]
    south_coord = [coord1[0]+1,coord1[1]]
    east_coord = [coord1[0],coord1[1]+1]
    west_coord = [coord1[0],coord1[1]-1]
    coordinates = [north_coord,south_coord,east_coord,west_coord]
    for coordinate in coordinates:
        test_color = samecolor(img, coord1, coordinate)
        test_is_starting = valueInList(coordinate,starting)
        test_in_boundary = valueInList(coordinate,boundary)
        if not(test_color or test_is_starting or test_in_boundary): #If the current point around the point is either the same color, a starting point, or is the boundary, Nothing suspicious, otherwise, this point is not done
            return False
            #For every coordinate up,down,left,right.. If it not the same color of the original coordinate, or is not a boundary, then we need to fill this still.
    return True
    #Otherwise, return true.
def remove_duplicates(coordinates:list[list[int,int]]) -> list[list[int,int]]:
    """Take a list of integer pairs and remoev all coordinates that appear more than once"""
    return_list = []
    for i in range(len(coordinates)):
        appears = False
        for j in range(len(coordinates)):
            same_y = coordinates[i][0]==coordinates[j][0]
            same_x = coordinates[i][1]==coordinates[j][1]
            if i<j and same_x and same_y:
                appears = True
        if not appears:
            return_list.append(coordinates[i])
    return return_list
def coordConv(coordinates:list[list[int,int]]) -> list[list[int,int]]:
    """Take a list of coordinates in the form of [x,y] and return them in the form of [y,x]"""
    return_list = []
    for coordinate in coordinates:
        return_list.append([coordinate[1],coordinate[0]])
    return return_list

def coordAdd(coordinates: list[list[int,int]], op:int=0) -> list[list[int,int]]:
    """Take a coordinate list and add one to every single value of the coordinate
    to go from a system starting from (0,0) to a system starting from (1,1)
    0 subtracts one, 1 adds one"""
    return_list = []
    if (op==0):
        for coordinate in coordinates:
            return_list.append([coordinate[0]-1,coordinate[1]-1])
    else:
        for coordinate in coordinates:
            return_list.append([coordinate[0]+1,coordinate[1]+1])
    return return_list




#Start state, check all the area around it, then color the north, south, east, and west of that point
#  For each point, check if all the area around it is the same color, or a boundary if so, then remove it from the list of potential points
#Otherwise, rerun the loop and do it until the entire area is filled.



def runalgo(img: np.ndarray,starting: list[list[int,int]], boundary:list[list[int,int]],input_color: list[int,int,int]) -> Union[list[int,int],None]:
    """Given a image, a starting position, and a boundary, run the algorithm on that image.
        Basically, start at the seed, and fill up the image with the boundary with our color.
        Both starting and boundary are in the form of [y,x]

    """
    directions = ["N","S","E","W"]
    test_points = copy.deepcopy(starting) #These are the points we must check and seed, we start at our starting point
    tracked = 0
    for coordinate in starting:
        img[coordinate[0],coordinate[1]] = input_color

    while len(test_points)!=0:
        new_points = []
        #These are all the new points we get from coloring all the points
        for i in range(len(test_points)):
            current_point = test_points[i]
            num = random.randint(0,9)
            if num<=6: #There is a 70% chance this will advance
                for direction in directions:
                    num2 = random.randint(0,9)
                    if num2<=5: #There is 60% chance we will move in any direction.
                        new_coord = color(img,current_point[0],current_point[1],boundary,img[current_point[0],current_point[1]],direction)
                        if new_coord is not None:
                            new_points.append(new_coord)
                    #For each coordinate, color the top, bottom, left, and right. Append each of these coordinates to the new list.
        test_points = test_points+new_points #Union the list with the new points added.
        #hotfix below, this is very costy in time, but saves us duplies
        #plt.imshow(img)
        #plt.show()
        finished_points = [] #Theses are all the points we want to keep
        for j in range(len(test_points)):
            current_point = test_points[j]
            if current_point is not None and not isPointDone(img, current_point, boundary, starting):
                finished_points.append(current_point)
        test_points = finished_points #After getting all the points we want, append them.
        test_points = remove_duplicates(test_points)
        tracked = tracked+1
#h
        # img3 = np.copy(img)
        # for point in test_points:
        #     img3[point[0],point[1]] = [255,255,255]
        #     plt.imshow(img3)
        # plt.show()

        img3 = Image.fromarray(img)
        img3.save('testrgb' + str(tracked) + '.png')



# img = np.array(Image.open('./uwah2.png'))
# #test = algorithmGUI('./uwah2.png')
#
# #test.displayGUI()
#
# #color(img, 4, 4, [], [255, 255, 255])
# #color(img, 4, 4, [], [255, 0, 0],"S")
# #color(img, 4, 4, [], [0, 255, 0],"N")
# #color(img, 4, 4, [], [0, 0, 255],"E")
# #color(img, 4, 4, [], [255, 255, 0],"W")
# test_boundary = [[25, 21],[26, 21],[27, 21],[27, 20],[28, 20],[29, 20],[30, 20],[31, 20],[32, 20],[32, 21],[29, 24],[28, 24],[27, 25],[26, 25],[25, 25],[25, 24],[25, 23],[25, 22],[25, 21],[26, 20],[31, 21],[31, 22],[30, 22],[29, 24],[29, 25],[29,23],[30,23]]
# #test_boundary = coordAdd(test_boundary)
# test_boundary = coordConv(test_boundary)
# start_state = [23-1,27-1]
#
#
# #test_boundary = [[27,23]]
# # img2 = np.array(Image.open('./uwah2.png'))
# # for coordinate in test_boundary:
# #     img2[coordinate[0]-1,coordinate[1]-1] = [255,255,0]
# # start_state = [23-1,27-1]
# # test_boundary.append([23-1,27-1-1])
# # #start_state = [23,27]
# # plt.imshow(img2)
# # plt.show()
# runalgo(img,start_state,test_boundary)
#
# #test #1
# img = np.array(Image.open('./uwah2.png'))
# test_boundary = [[25, 21],[26, 21],[27, 21],[27, 20],[28, 20],[29, 20],[30, 20],[31, 20],[32, 20],[32, 21],[29, 24],[28, 24],[27, 25],[26, 25],[25, 25],[25, 24],[25, 23],[25, 22],[25, 21],[26, 20],[31, 21],[31, 22],[30, 22],[29, 24],[29, 25],[29,23],[30,23]]
# #test_boundary = coordAdd(test_boundary)
# test_boundary = coordConv(test_boundary)
# start_state = [23-1,27-1]
# runalgo(img,start_state,test_boundary)
# test #2

# img2 = np.array(Image.open('./square.png'))
# start_state = [[50,50],[25,25],[69,11]]
# test_boundary = []
# for i in range(0,80):
#     test_boundary.append([10,10+i])
#     test_boundary.append([80,10+i])
#     test_boundary.append([10+i,10])
#     test_boundary.append([10+i,80])
#
# for coordinate in test_boundary:
#     img2[coordinate[0],coordinate[1]] = [255,255,0]
# # plt.imshow(img2)
# # plt.show()
# runalgo(img2,start_state,test_boundary)

