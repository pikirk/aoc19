import sys

# https://adventofcode.com/2019/day/4#part1
start = 265275
end = 781584
met = 0
for num in range (start, end, 1):
    digits = [int(x) for x in str(num)] 
    index = len(digits)
    seenDouble = False
    decreasing = False
    cur = -1

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

        # check for double
        if ( ( i - 1 ) >= 0 ) and not seenDouble:
            next = digits[i-1]
            seenDouble = (cur == next)

    if (seenDouble and decreasing):
        met = met + 1

print('Met = ' + str(met))