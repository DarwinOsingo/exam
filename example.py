#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING s as parameter.
#

def isValid(s):
    stack = []
    comp = {
        '(':')',
        '[':']',
        '{':'}'
    }
    for char in s:
        if char in comp:
            stack.append(char)
        else:
            if not stack:
                return False
            last = stack.pop()
            if comp[last] != char:
                return False
    return len(stack)== 0
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(str(result) + '\n')

    fptr.close()