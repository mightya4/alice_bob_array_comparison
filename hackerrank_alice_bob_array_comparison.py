#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    #initialize integer array
    integerArray = [0,0]
    index = 0
    for i in range(index, len(a)):
        #array a gets 1 point
        if a[i] > b[i]:
            integerArray[0] += 1
        #array b gets 1 point
        if a[i] < b[i]:
            integerArray[1] += 1
        #no one gets a point
        if a[i] == b[i]:
            pass
    return integerArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
