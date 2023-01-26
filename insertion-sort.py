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
    #[1,2,,3,4,5,6]
    #  i i+1
    comp = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i] > comp:
            arr[i+1]=arr[i]
            print(" ".join(str(i) for i in arr))
        if i==0 and arr[i]> comp:
            arr[i]=comp
            print(" ".join(str(i) for i in arr))
        elif arr[i]<=comp:
            arr[i+1]=comp
            print(" ".join(str(i) for i in arr))
            break
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
