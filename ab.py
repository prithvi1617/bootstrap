#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    d1=0
    d2=0
    # Write your code here
    print(len(arr))
    print(arr)
    for i in range(len(arr)):
        
        for j in range(len(arr)):
            if(i==j):
                d1+=arr[i][j]
    m=0
    l= len(arr)-1 

    for k in range(len(arr)):
        d2+=arr[m][l]
        m+=1
        l-=1
        

    print(d1,d2)
    # if(d1>d2):
    #     return d1-d2
    # else:
    #     return d2-d1


        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
