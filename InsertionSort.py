#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    last = arr[n - 1]
    for i in range(n - 2, -1, -1):
            
        if last > arr[i]:
            arr[i + 1] = last
            break
        else:
            arr[i + 1] = arr[i]
            print(' '. join(str(x) for x in arr))
    if arr[0] == arr[1]:
        arr[0] = last
    print(' '.join(str(x) for x in arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
