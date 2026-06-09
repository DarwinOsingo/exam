#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minMoves(arr):
    arr.sort()

    median = arr[len(arr)//2]
    step= 0
    for num in arr:
        value =abs(num-median)
        step += value
    return step

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minMoves(arr)

    fptr.write(str(result) + '\n')

    fptr.close()