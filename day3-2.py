import copy
import sys

DIR = 0
LEN = 1

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.s = str(x) + ',' + str(y)
        self.intersection = False

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

def parse(inputPath:str) -> []:
    return inputPath.split(',')

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
            p = Point( origin[0] + (x + 1), origin[1])
            pts.append(p)

    elif dir == 'L':
        for x in range(len):
            p = Point(origin[0] - (x + 1), origin[1])
            pts.append(p)

    elif dir == 'U':
        for x in range(len):
            p = Point( origin[0], origin[1] + (x + 1) )
            pts.append(p)
    
    elif dir == 'D':
        for x in range(len):
            p = Point(origin[0], origin[1] - (x + 1) )
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
    origin = [0,0]
    pts = []
    pts.append( Point(origin[0], origin[1] ) )
    specs = parse(specPath)
    for s in range(len(specs)):  
        spec = parseSpec(specs[s])
        pts = pts + expand(origin, spec[DIR], spec[LEN])
        origin = nextPoint(origin, spec[DIR], spec[LEN])
        retval = pts
    
    return retval   

def calculateShortestPath(path:list, intersections:set) -> int:
    print ('TODO')
    return -1

################################################
## Start Puzzle Processing
################################################

# read puzzle input
inputs = open('test.txt', 'r').readlines()

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

# mark the points that intersect in the line lists
# TODO Refactor to lambda object query (LINQ)
for hash in diff:
    for index in range(len(line1)):
        if hash == line1[index].s:
            line1[index].intersection = True

    for index in range(len(line2)):
        if hash == line2[index].s:
            line2[index].intersection = True

# walk the steps to get to each intersection

