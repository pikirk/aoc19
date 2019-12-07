def nextPoint (origin, dir, len):
    if dir == 'R':
        return [(origin[0] + len), origin[1]]
    elif dir == 'L':
        return [(origin[0] - len), origin[1]]
    elif dir == 'U':
        return [origin[0], (origin[1] + len)]
    elif dir == 'D':
        return [origin[0], (origin[1] - len)]
    else:
        raise Exception('Bad direction')

def hitTest(pt1, pt2):
    if (pt1[0] == pt2[0]) and (pt1[1] == pt2[1]): return True
    return False

def distanceToPort(pt):
    return abs(pt[0]) + abs(pt[1])

def readAndParse():
    # TODO input = open("day3-1-input.txt", "r").readlines()
    return [ [{}], [{}] ]

# outline
# read and parse input
# starting at origin (0,0) calculate next point for each direction code
# peform a hit test on the next points
# if true, add to intersection list
# get the shortest distance from origin (0,0) for all intersections

# test inputs
pinkPath = ['R1009','U263','L517','U449','L805','D78','L798','D883'',L777','D562']
bluePath = ['L1003','D960','L10','D57','R294','U538','R867','D426','L524','D441','R775','U308']


