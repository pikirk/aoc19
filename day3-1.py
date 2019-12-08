import copy

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

# ex. R456,U344,D4566
def parse(inputs):
    retValue = []
    for i in range( len(inputs) ):
        s = inputs[i]
        retValue.append( list( (s.split(',') ) ) )
    return retValue

# ex. R456
def parseSpec(spec):
    dir = spec[0]
    take = len(spec)
    size = spec[1:take] 
    return [dir, int (size.strip())]

# # plots both lines based on the direction specs and
# # evaluates if lines intersect during the plot
# # we only have 2 lines to worry about for this puzzle
# def plotAndEval(paths):
#     retValue = []

#     ob = 0
#     if len(paths[0]) > len(paths[1]):                       # determine max outer boundary
#         ob = len(paths[0])
#     else: 
#         ob = len(paths[1]) 

#     origin1 = [0,0] 
#     origin2 = [0,0]

#     for curIndex in range(ob):
#         first = parseSpec(paths[0][curIndex])               # plot first line
#         pt1 = nextPoint(origin1, first[0], first[1])
#         origin1 = pt1
                                            
#         if ( curIndex <= len(paths[1]) ):                   # plot second line
#             second = parseSpec(paths[1][curIndex])  
#             pt2 = nextPoint(origin2, second[0], second[1])
#             origin2 = pt2

#         if (hitTest(pt1, pt2)):
#             retValue.append(pt1)
    
#     return 

def plotPoints(path):
    line = set()
    origin = [0,0]
    for index in range(len(path)):
        spec = parseSpec(path[index])
        next = nextPoint(origin, spec[0], spec[1])
        line.add(str(next[0]) + ',' + str(next[1]))
        origin = next
    return line

def plotAndEval(paths):
    firstSet = plotPoints(paths[0])
    secondSet = plotPoints(paths[1])
    diff = firstSet.intersection(secondSet)   # get the common points in poth sets
    print(diff)


# outline
# read and parse input
# starting at origin (0,0) calculate next point for each direction code
# peform a hit test on the next points
# if true, add to intersection list
# get the shortest distance from origin (0,0) for all intersections

# test inputs
inputs = open('test.txt', 'r').readlines()
result = parse(inputs)
plotAndEval(result)



