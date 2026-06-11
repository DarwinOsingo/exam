# Problem: Maximum Subarray Sum (Kadane's Algorithm)
# Given an integer array, find the contiguous subarray with the largest sum and return that sum.
# Example:
# Input:  arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# ([4, -1, 2, 1] has the largest sum = 6)

# HackerRank Starting Point:
# python#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maxSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()