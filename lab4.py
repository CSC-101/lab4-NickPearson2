import data
import math
# Write your functions for each part in the space below.

# Part 1
def first_element(theList):
    f_element_list = []
    for i in theList:
        if(i!=[]):
            f_element_list.append(i[0])
    return f_element_list

# Part 2
def x_coordinates(theList):
    x_coords = []
    for i in theList:
        if(type(i) == data.Point):
            x_coords.append(i.x)
    return x_coords
# Part 3
def are_in_positive_quadrant(theList):
    first_q = []
    for i in theList:
        if(type(i) == data.Point):
            if(i.x >0 and i.y >0):
                first_q.append(i)

# Part 4
def distance(point1,point2):
    dist_x = point1.x - point2.x
    dist_y = point1.y - point2.y
    e_distance= math.sqrt(dist_x**2 + dist_y**2)
    return e_distance

# Part 5
def manhattan_distance(point1,point2):
    x_dist = (point1.x-point2.x)
    y_dist = (point1.y-point2.y)
    return x_dist + y_dist

# Part 6
def distance_all(pointList):
    origin = data.Point(0,0)
    all_distance = []
    for i in pointList:
        d = distance(origin,i)
        all_distance.append(d)
    return all_distance


