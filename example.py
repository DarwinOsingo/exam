# Problem: Find Missing Number
# Given an array of n-1 integers in the range [1, n], find the one missing number. Every number appears exactly once except for the missing one.
# Example:
# Input:  arr = [1, 2, 4, 5, 6], n = 6
# Output: 3
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMissing' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER n
#

# def findMissing(arr, n):
#     arr.sort()
#     for i in range(len(arr)):
#         if arr[i] != i+1:
#             return i + 1
#     return n
    

def findMissing(arr, n):
    formula = n*(n+1)//2
    arr_sum = sum(arr)
    return formula- arr_sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMissing(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()