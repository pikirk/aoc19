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
    segments = []
    for pt in intersections:
        c = 0
        for p in path:
            c = c + 1
            if ( (p.intersection and p.s == pt) and p.s != '0,0'):
                segments.append(c-1)
                c = 0
    if (any(segments)):       
        return min(segments)
    else:
        return segments

def findIntersections(path:[]) -> set:
    """
    Finds coordinates where a path intersects itself
    """
    retval = set()
    seen = set()
    for c in path:
        xy = Point.toString(c.x, c.y)
        if xy not in seen:
            seen.add(xy)
        else:
            retval.add(xy)
    return retval


################################################
## Start Puzzle Processing
##
## https://adventofcode.com/2019/day/3#part2
################################################

# read puzzle input
inputs = open('test.txt', 'r').readlines()

# plot lines
path1 = plotPoints(inputs[0])
path2 = plotPoints(inputs[1])

# find intersection within each line
int1 = findIntersections(path1)
int2 = findIntersections(path2)

# hash the stringified coordinates
line1PointSet = set()
line1PointSet.update( (obj.s for obj in path1) )
line2PointSet = set()
line2PointSet.update( (obj.s for obj in path2 ) )

# find common points in both sets - these represent
# the line intersections
diff = set()
diff = line1PointSet.intersection(line2PointSet)
diff.update(int1)
diff.update(int2)


# mark the points that intersect in the line lists
# TODO Refactor to lambda object query (LINQ)
for hash in diff:
    for index in range(len(path1)):
        if hash == path1[index].s:
            path1[index].intersection = True

    for index in range(len(path2)):
        if hash == path2[index].s:
            path2[index].intersection = True

# walk the steps to get to each intersection
result = calculateShortestPath(path1, diff) + calculateShortestPath(path2, diff)
print (str(result))


# # print specs as x,y
# r = parse(inputs[1])
# xy = []
# origin = [0,0]
# for item in r:
#     spec = parseSpec(item)
#     tmp = nextPoint(origin, spec[DIR], spec[LEN])
#     xy.append(tmp)
#     origin = tmp
#     print (tmp)




