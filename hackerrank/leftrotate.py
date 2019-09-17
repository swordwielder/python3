#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    b=[]
    index=0
    for i in range(d):
        b.append(a[i])
    print ("b ", b)
    loops = len(a)-d
    replace=d
    for j in range(loops):
        a[j]=a[replace]
        replace+=1
    print(a,"a")
    for i in range (len(a)-d,len(a)):
        a[i]=b[index]
        index+=1
    print(a,"a")
    
    return a
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    #print(a)
    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

