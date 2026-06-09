#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#

def twoSum(arr, target):
    seen = {}
    for i,num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num]= i

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    target = int(input().strip())

    result = twoSum(arr, target)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()