#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name = []
    name = s.split()
    capname = ""
    for i in name:
        capname+=i.capitalize()+" "
    return capname

    return(string.capwords(s, ' '))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

