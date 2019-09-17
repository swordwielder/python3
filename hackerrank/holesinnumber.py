#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countHoles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER number as parameter.
#

def countHoles(number):
    # Write your code here
    test = str(number)
    count=0

    for i in test:
        if float(i)==0 or float(i)==4 or float(i)==6 or float(i)==9:
            count+=1
        elif float(i)==8:
            count+=2

    return count
    

if __name__ == '__main__':
