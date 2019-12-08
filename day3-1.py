import copy
import sys

DIR = 0
LEN = 1

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.s = str(x) + ',' + str(y)
    
    @staticmethod
    def toString(x:int, y:int) -> str:
        return str(x) + ',' + str(y)
    
    @staticmethod
    def toArray(xy:str) -> []:
        c = xy.split(',')
        c[0] = int(c[0]) 
        c[1] = int(c[1])
        return c
    
def nextPoint (origin:[], dir:str, len:int) -> []:
    """
    For a given direction and length, calculates the next cartesian
    point
    """
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

def parse(inputPath):
    return inputPath.split(',')

# ex. R456
def parseSpec(spec:str) -> []:
    """
    Parses a path instruction
    Ex. R345 yield ['R',345]
    """
    dir = spec[0]
    take = len(spec)
    size = spec[1:take] 
    return [dir, int (size.strip('\n'))]

def expand (origin:[], dir:str, len:int) -> []:
    """
    Calculates all cartesian coordinates from a start point
    for a zero slope segment
    """
    pts = []
    if dir == 'R':
        for x in range(len):
            p = Point( origin[0] + (x+1), origin[1])
            pts.append(p)

    elif dir == 'L':
        for x in range(len):
            p = Point(origin[0] - (x+1), origin[1])
            pts.append(p)

    elif dir == 'U':
        for x in range(len):
            p = Point( origin[0], origin[1] + (x+1) )
            pts.append(p)
    
    elif dir == 'D':
        for x in range(len):
            p = Point(origin[0], origin[1] - (x+1))
            pts.append(p)
    else:
        raise Exception('Bad direction')

    return pts

def plotPoints(specPath:[]) -> []:
    """
    Evaluates line instructions in the spec path and calculates all cartesian
    coordinate in each segment
    """
    retval = []
    seen = set()
    origin = [0,0]
    seen.add(Point.toString(0,0))
    specs = parse(specPath)
    for s in range(len(specs)):                         # need to de-dupe start/end pts
        spec = parseSpec(specs[s])
        pts = expand(origin, spec[DIR], spec[LEN])
        pts.append( Point(origin[0], origin[1] ) )
        origin = nextPoint(origin, spec[DIR], spec[LEN])
        retval = retval + pts
    
    return retval   

def calculateClosest(pts:set) -> int:
    """
    Calculates the closest manhattan distance for all points
    based on 0,0 origin
    """
    retval = 0
    index = 0
    for hash in pts:
        p = Point.toArray(hash)
        d = abs(p[0]) + abs(p[1])

        if ( index == 0 ):
            retval = d
        elif( d > 0 and d < retval):
            retval = d

        index = index + 1

    return retval

################################################
## Start Puzzle Processing
################################################

# read puzzle input
inputs = open('day3-1-input.txt', 'r').readlines()

# plot lines
line1 = plotPoints(inputs[0])
line2 = plotPoints(inputs[1])

# hash the stringified coordinates
line1PointSet = set()
line1PointSet.update( obj.s for obj in line1 )
line2PointSet = set()
line2PointSet.update( obj.s for obj in line2 )

# find common points in both sets - these represent
# the line intersections
diff = line1PointSet.intersection(line2PointSet)

# calculate manhattan distance
d = calculateClosest(diff)
print('Answer = ' + str(d))



