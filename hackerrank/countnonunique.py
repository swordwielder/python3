#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countNonUnique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#
from itertools import groupby
def countNonUnique(numbers):
    
    numbers.sort()
    a = [len(list(group)) for key, group in groupby(numbers)]
    count=0
    for i in a:
        if i >1:
            count+=1
    return count

    # Write your code here

if __name__ == '__main__':
