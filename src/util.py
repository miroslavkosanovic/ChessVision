from itertools import tee, izip
import cv2
import numpy as np
from numpy import matrix, array, dot, transpose

##  cooordinate conversions

#function: board_to_image_coords
#BIH: board to image projective transformation
#board_coords: coordinates of point in board coordinates
#returns: image coordinates of the aforementioned point

def board_to_image_coords(BIH, board_coords):
    return dehomogenize(BIH * homogenize(board_coords))

#function: image_to_board_coords
#BIH: board to image projective transformation
#image_coords: coordinates of point in image coordinates
#returns: board coordinates of the aforementioned point

def image_to_board_coords(BIH, image_coords):
    return dehomogenize(inv(BIH) * homogenize(image_coords))









##  points

#function: homogenize
#x: tuple 
#returns: numpy array represented in homogenous coordinates
def homogenize(x):
    return transpose(matrix ((x[0],x[1], 1)))

#function: dehomogenize
#x: homogenous vector 
#returns: tuple
def dehomogenize(x):
    x= list(array(x).reshape(-1,))
    return (x[0]/x[2], x[1]/x[2])

#function: euclidian_distance
#p1,p2: two points as 2-tuples 
#returns: euclidean distance between given points

def eucledian_distance(p1,p2):
    assert ((len(p1)==len(p2)) and len(p2) == 2)
    return np.sqrt((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2)

#function: get_centroid(points):
#points: a list of points represented as 2-tuples
#returns: the centroid of points
def get_centroid(points):
    return (np.mean([p[0] for p in points]), np.mean([p[1] for p in points]))