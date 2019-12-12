import sys
# https://adventofcode.com/2019/day/4#part2

start = 265275
end = 781584
met = 0
for num in range (start, end, 1):
    digits = [int(x) for x in str(num)] 
    index = len(digits)
    double = []
    decreasing = False
    cur = -1

    foundDouble = False
    validDouble = False

    # walk backwards through the digits
    for i in range( len(digits) - 1, -1, -1 ):

        # check for decreasing digits
        if ( i == len(digits) -1 ):
            cur = digits[i]
        else:
            if ( digits[i] <= cur ):
                cur = digits[i]
                decreasing = True
            else:
                decreasing = False
                break

        peek = ( i-1 ) >= 0
        next = digits[i-1]
        eon = ( i == len(digits) -1 )
        emptyDouble = len(double) == 0
        if peek:
            if (not foundDouble and (next == cur)):
                foundDouble = True
                double = [next, cur]
                validDouble = foundDouble
                
            elif foundDouble:
                if not eon and next == 1 and not emptyDouble and double[0] == next:
                    print ('Ones check...')
                elif not emptyDouble and next < cur:        # new double test
                    double = []
                elif not emptyDouble and next == double[0]: # bad double (breaks adjacent digit rule)
                    validDouble = False
                    break
                elif cur == next:                           # set new double for next iteration test
                    double = [next, cur]


    if foundDouble:
        if (validDouble and decreasing):
            met = met + 1
    elif decreasing:
        met = met + 1

print('Met = ' + str(met))
